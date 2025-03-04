# UpdateInfectedFilesParameters

Specifies the parameters of infected files to be updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infected_files** | [**List[InfectedFile]**](InfectedFile.md) | Specifies a list of infected files to be updated. | 
**state** | **str** | Specifies the state[Quarantined, Unquarantined] of the infected file. | [optional] 

## Example

```python
from cohesity_sdk.models.update_infected_files_parameters import UpdateInfectedFilesParameters

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInfectedFilesParameters from a JSON string
update_infected_files_parameters_instance = UpdateInfectedFilesParameters.from_json(json)
# print the JSON string representation of the object
print(UpdateInfectedFilesParameters.to_json())

# convert the object into a dict
update_infected_files_parameters_dict = update_infected_files_parameters_instance.to_dict()
# create an instance of UpdateInfectedFilesParameters from a dict
update_infected_files_parameters_from_dict = UpdateInfectedFilesParameters.from_dict(update_infected_files_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


