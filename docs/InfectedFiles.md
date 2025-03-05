# InfectedFiles

Specifies a list of infected files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookie** | **str** | Specifies the pagination cookie. Cookie is used to  resume the enumeration of infected files. When the cookie is set the fields viewNameVec, includeQuarantinedFiles and includeUnquarantinedFiles are ignored.  | [optional] 
**infected_files** | [**List[InfectedFile]**](InfectedFile.md) | Specifies the list of infected files. | [optional] 

## Example

```python
from cohesity_sdk.models.infected_files import InfectedFiles

# TODO update the JSON string below
json = "{}"
# create an instance of InfectedFiles from a JSON string
infected_files_instance = InfectedFiles.from_json(json)
# print the JSON string representation of the object
print(InfectedFiles.to_json())

# convert the object into a dict
infected_files_dict = infected_files_instance.to_dict()
# create an instance of InfectedFiles from a dict
infected_files_from_dict = InfectedFiles.from_dict(infected_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


