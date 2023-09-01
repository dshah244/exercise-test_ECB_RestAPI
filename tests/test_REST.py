import pathlib as pl
import pytest
import re
import requests

@pytest.mark.parametrize("cur", ["USD", "GBP", "PLN"])
def test_data_JPY_OR(cur):
    """
    Test checks whether the usage of OR 'key' in the ECB REST APID works as intended.
    
    **Test design**

    Extract monthly data from ECB server for three combionations of currencies.
    
    1) USD + JPY against EUR
    2) GBP + JPY against EUR
    3) PLN + JPY against EUR

    **Expectation**

    1) There are two instances of entry 'CURRENCY' present within downloaded data, 'USD' and 'JPY', respectively.
    2) There are two instances of entry 'CURRENCY' present within downloaded data, 'GBP' and 'JPY', respectively.
    3) There are two instances of entry 'CURRENCY' present within downloaded data, 'PLN' and 'JPY', respectively.
      
    The value of instance 'CURRENCY_DENOM' is always 'EUR' for each combination.

    """

    url = f"https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.{cur}+JPY.EUR.SP00.A"
    req = requests.get(url)
    req_content = req.content
    currency = []
    for one_line in req_content.decode("utf-8").split("\n"):
        if '\"CURRENCY\"' in one_line:
            currency += re.findall(pattern='\"CURRENCY\".*value=\"(.*[A-Z])\"', string=one_line)
        elif '\"CURRENCY_DENOM\"' in one_line:
            find_pattrn = set(re.findall(pattern='\"CURRENCY_DENOM\".*value=\"(.*[A-Z])\"', string=one_line))
            assert "EUR" in find_pattrn, "ERROR: Exchange rates are NOT against Euros!"
            assert len(find_pattrn) == 1, "ERROR: Exchange rates are NOT only  against Euros!"
    assert 'JPY' in currency, "ERROR: requested currency JPY not retrieved!"
    assert cur in currency, "ERROR: requested currency USD not retrieved!"
    assert len(currency) == 2, "ERROR: More than requested currencies found!"

def test_data_if_modified_since():
    """
    Test checks whether If-Modified-Since functionality works on the ECB server.
    
    **Test design**

    Communicate to the ECB server a timestamp in the future.
    Future timestamp should be at a later point than the timestamp communicated by the server using 'last-modified' header.
    
    **Expectation**
    
    Communicated timestamp to the server using 'If-Modified-Since' is in the future relative to the timestamp
    provided by the server as read using 'last-modified'.

    Requesting the server for content should result in status code 304 instead of 200.
    With a status code: 304, no content should be sent by the server.

    
    **Observation**

    ECB server does not seem to function as expected.
    Communication of a future timestamp does not result is a status code: 304.

    Content is still downloaded.

    """

    url = "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/D.JPY.EUR.SP00.A/"

    # req.headers["last-modified"] is found to be "Mon, 05 Jul 2021 13:56:50 GMT"
    dict_headers = {"if-modified-since": "Mon, 11 Oct 2021 15:00:00 GMT"}
    req = requests.get(url, headers=dict_headers)

    assert req.status_code == 304, "ERROR: If-Modified-Since header does NOT work.\n"\
                                   f"last-modified timestamp: {req.headers['last-modified']}\n"\
                                   f"if-modified-since timestamp: {dict_headers['if-modified-since']}"
    assert b'No results found.' == req.content, "ERROR: Unexpected content is being sent by the server!"

def test_http():
    """
    Test checks for HTTP URL being re-directed to HTTPS protocol.

    **Test design**

    Send a request to the server using HTTP protocol.

    
    **Expectation**

    URL communicated by the server follows HTTPS protocol.

    """

    url = "http://sdw-wsrest.ecb.europa.eu/service/data/EXR/D.JPY.EUR.SP00.A/"
    req = requests.get(url)
    assert not ("http:" in req.url), "ERROR: 'http' is NOT re-directed to 'https' protocol"


def test_robust_flowref():
    """
    This test case is used to check basic functionality of the REST API provided ECB.
    `flowRef` needs to be provided as comma separated value of `AGENCY_ID,FLOW_ID,VERSION` to the server.
    In this test case, an invalid `AGENCY_ID` is provided to the server.

    **Test Design**

    Provide an invalid value to `AGENCY_ID` and `FLOW_ID`.

    **Expectation**

    Server communicates status code: 404.
    No data is recovered.

    """
    url = "http://sdw-wsrest.ecb.europa.eu/service/data/dshah"
    req = requests.get(url)
    assert req.status_code == 404, "ERROR: Server responds to erroneous data."
    assert b'No results found.' == req.content, "ERROR: Unexpected content is being sent by the server!"

def test_other_specs():
    """
    Other testing areas of importance are as follows:

    * Tests which validate the status code sent by the server to the client.
      Example, Status code: 406
    * Tests validating the supported data-formats such as: JSON, CSV, SDMX-ML...
    * Tests validating the support for possible values of different entries such as resource, flowRef, key, agencyID, resoueceID, version, timestamps.
    * Tests which validate the use of combination of parameters
        - using starPeriod and endPeriod together.
        - using firstNObservations and lastNObservations together.
        - using one parameter twice. Example, `detail=full&detail=dataonly`.
    * Validate data-compression using header `Accept-Encoding HTTP header`    

    """
    assert True, "Please check the documentation for potential test areas."\
                 "Documentation: pt_m/html/index.html"
