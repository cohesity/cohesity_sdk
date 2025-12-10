# DB2Params

Specifies the recovery options specific to DB2 environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_db2_params** | [**RecoverDB2Params**](RecoverDB2Params.md) |  | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.cluster.models.db2_params import DB2Params

# TODO update the JSON string below
json = "{}"
# create an instance of DB2Params from a JSON string
db2_params_instance = DB2Params.from_json(json)
# print the JSON string representation of the object
print(DB2Params.to_json())

# convert the object into a dict
db2_params_dict = db2_params_instance.to_dict()
# create an instance of DB2Params from a dict
db2_params_from_dict = DB2Params.from_dict(db2_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


