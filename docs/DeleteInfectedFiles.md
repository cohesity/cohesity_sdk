# DeleteInfectedFiles

Specifies a list of infected files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_failed_infected_files** | [**List[InfectedFile]**](InfectedFile.md) | Specifies the list of infected files that failed deletion. | [optional] 
**delete_succeeded_infected_files** | [**List[InfectedFile]**](InfectedFile.md) | Specifies the list of infected files that are successfully deleted. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.delete_infected_files import DeleteInfectedFiles

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteInfectedFiles from a JSON string
delete_infected_files_instance = DeleteInfectedFiles.from_json(json)
# print the JSON string representation of the object
print(DeleteInfectedFiles.to_json())

# convert the object into a dict
delete_infected_files_dict = delete_infected_files_instance.to_dict()
# create an instance of DeleteInfectedFiles from a dict
delete_infected_files_from_dict = DeleteInfectedFiles.from_dict(delete_infected_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


