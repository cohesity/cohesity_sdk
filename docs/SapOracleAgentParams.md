# SapOracleAgentParams

SapOracle agent parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_type** | **str** | Specifies the type of installer. | 

## Example

```python
from cohesity_sdk.models.sap_oracle_agent_params import SapOracleAgentParams

# TODO update the JSON string below
json = "{}"
# create an instance of SapOracleAgentParams from a JSON string
sap_oracle_agent_params_instance = SapOracleAgentParams.from_json(json)
# print the JSON string representation of the object
print(SapOracleAgentParams.to_json())

# convert the object into a dict
sap_oracle_agent_params_dict = sap_oracle_agent_params_instance.to_dict()
# create an instance of SapOracleAgentParams from a dict
sap_oracle_agent_params_from_dict = SapOracleAgentParams.from_dict(sap_oracle_agent_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


