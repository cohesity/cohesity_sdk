# UpdateInfectedFilesList

Specifies a list of infected files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_failed_infected_files** | [**List[InfectedFile]**](InfectedFile.md) | Specifies the list of infected files that failed update. | [optional] 
**update_succeeded_infected_files** | [**List[InfectedFile]**](InfectedFile.md) | Specifies the list of infected files that are successfully updated. | [optional] 

## Example

```python
from cohesity_sdk.models.update_infected_files_list import UpdateInfectedFilesList

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInfectedFilesList from a JSON string
update_infected_files_list_instance = UpdateInfectedFilesList.from_json(json)
# print the JSON string representation of the object
print(UpdateInfectedFilesList.to_json())

# convert the object into a dict
update_infected_files_list_dict = update_infected_files_list_instance.to_dict()
# create an instance of UpdateInfectedFilesList from a dict
update_infected_files_list_from_dict = UpdateInfectedFilesList.from_dict(update_infected_files_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


