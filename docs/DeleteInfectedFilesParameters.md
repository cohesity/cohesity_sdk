# DeleteInfectedFilesParameters

Specifies the parameters to delete infected files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infected_files** | [**List[InfectedFile]**](InfectedFile.md) | Specifies a list of infected files to be deleted. | 

## Example

```python
from cohesity_sdk.models.delete_infected_files_parameters import DeleteInfectedFilesParameters

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteInfectedFilesParameters from a JSON string
delete_infected_files_parameters_instance = DeleteInfectedFilesParameters.from_json(json)
# print the JSON string representation of the object
print(DeleteInfectedFilesParameters.to_json())

# convert the object into a dict
delete_infected_files_parameters_dict = delete_infected_files_parameters_instance.to_dict()
# create an instance of DeleteInfectedFilesParameters from a dict
delete_infected_files_parameters_from_dict = DeleteInfectedFilesParameters.from_dict(delete_infected_files_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


