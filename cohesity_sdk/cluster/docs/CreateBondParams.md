# CreateBondParams

Specifies the parameters needed to create a bond.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies a unique name to identify the bond being created. | 
**slaves** | **List[Optional[str]]** | Specifies the names of the secondaries of this bond. | 

## Example

```python
from cohesity_sdk.cluster.models.create_bond_params import CreateBondParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBondParams from a JSON string
create_bond_params_instance = CreateBondParams.from_json(json)
# print the JSON string representation of the object
print(CreateBondParams.to_json())

# convert the object into a dict
create_bond_params_dict = create_bond_params_instance.to_dict()
# create an instance of CreateBondParams from a dict
create_bond_params_from_dict = CreateBondParams.from_dict(create_bond_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


