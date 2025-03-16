# DownloadAgentRequestParams

Specifies agent download request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aix_params** | [**AixAgentParams**](AixAgentParams.md) |  | [optional] 
**linux_params** | [**LinuxAgentParams**](LinuxAgentParams.md) |  | [optional] 
**my_sql_params** | [**MySqlAgentParams**](MySqlAgentParams.md) |  | [optional] 
**platform** | **str** | Specifies the platform for which agent needs to be downloaded. | 
**sap_hana_params** | [**SapHanaAgentParams**](SapHanaAgentParams.md) |  | [optional] 
**sap_oracle_params** | [**SapOracleAgentParams**](SapOracleAgentParams.md) |  | [optional] 
**vmware_cdp_filter_params** | [**VMWareCDPFilterParams**](VMWareCDPFilterParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.download_agent_request_params import DownloadAgentRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadAgentRequestParams from a JSON string
download_agent_request_params_instance = DownloadAgentRequestParams.from_json(json)
# print the JSON string representation of the object
print(DownloadAgentRequestParams.to_json())

# convert the object into a dict
download_agent_request_params_dict = download_agent_request_params_instance.to_dict()
# create an instance of DownloadAgentRequestParams from a dict
download_agent_request_params_from_dict = DownloadAgentRequestParams.from_dict(download_agent_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


