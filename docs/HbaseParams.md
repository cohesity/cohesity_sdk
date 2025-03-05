# HbaseParams

Specifies the recovery options specific to Hbase environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_hbase_params** | [**RecoverHbaseParams**](RecoverHbaseParams.md) |  | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.models.hbase_params import HbaseParams

# TODO update the JSON string below
json = "{}"
# create an instance of HbaseParams from a JSON string
hbase_params_instance = HbaseParams.from_json(json)
# print the JSON string representation of the object
print(HbaseParams.to_json())

# convert the object into a dict
hbase_params_dict = hbase_params_instance.to_dict()
# create an instance of HbaseParams from a dict
hbase_params_from_dict = HbaseParams.from_dict(hbase_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


