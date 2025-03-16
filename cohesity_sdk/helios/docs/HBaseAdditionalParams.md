# HBaseAdditionalParams

Additional params for HBase protection source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | Authentication type. | [optional] [readonly] 
**data_root_directory** | **str** | The &#39;Data root directory&#39; for this HBase. | [optional] [readonly] 
**zookeeper_quorum** | **List[str]** | The &#39;Zookeeper Quorum&#39; for this HBase. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.h_base_additional_params import HBaseAdditionalParams

# TODO update the JSON string below
json = "{}"
# create an instance of HBaseAdditionalParams from a JSON string
h_base_additional_params_instance = HBaseAdditionalParams.from_json(json)
# print the JSON string representation of the object
print(HBaseAdditionalParams.to_json())

# convert the object into a dict
h_base_additional_params_dict = h_base_additional_params_instance.to_dict()
# create an instance of HBaseAdditionalParams from a dict
h_base_additional_params_from_dict = HBaseAdditionalParams.from_dict(h_base_additional_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


