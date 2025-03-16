# SapHanaAgentParams

SapHana agent parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_type** | **str** | Specifies the type of agent. kJava agent type is supported only for kScript package type. | 
**package_type** | **str** | Specifies the type of installer. | 

## Example

```python
from cohesity_sdk.helios.models.sap_hana_agent_params import SapHanaAgentParams

# TODO update the JSON string below
json = "{}"
# create an instance of SapHanaAgentParams from a JSON string
sap_hana_agent_params_instance = SapHanaAgentParams.from_json(json)
# print the JSON string representation of the object
print(SapHanaAgentParams.to_json())

# convert the object into a dict
sap_hana_agent_params_dict = sap_hana_agent_params_instance.to_dict()
# create an instance of SapHanaAgentParams from a dict
sap_hana_agent_params_from_dict = SapHanaAgentParams.from_dict(sap_hana_agent_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


