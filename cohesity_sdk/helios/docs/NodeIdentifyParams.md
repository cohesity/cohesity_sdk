# NodeIdentifyParams

Specifies the parameter to identify node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identify** | **bool** | Turn on/off node led light if set to true/false respectively. | 

## Example

```python
from cohesity_sdk.helios.models.node_identify_params import NodeIdentifyParams

# TODO update the JSON string below
json = "{}"
# create an instance of NodeIdentifyParams from a JSON string
node_identify_params_instance = NodeIdentifyParams.from_json(json)
# print the JSON string representation of the object
print(NodeIdentifyParams.to_json())

# convert the object into a dict
node_identify_params_dict = node_identify_params_instance.to_dict()
# create an instance of NodeIdentifyParams from a dict
node_identify_params_from_dict = NodeIdentifyParams.from_dict(node_identify_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


