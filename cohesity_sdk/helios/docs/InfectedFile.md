# InfectedFile

Specifies an infected file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**antivirus_service_group_name** | **str** | Specifies the Antivirus Service group which detected the threats. | [optional] 
**antivirus_service_icap_uri** | **str** | Specifies the ICAP Uri of the Antivirus Service which detected the threats. | [optional] 
**detected_time_usecs** | **int** | Specifies the timestamp in microseconds when the threats were detected. | [optional] 
**entity_id** | **int** | Specifies the entity id of the infected file. | 
**last_modified_time_usecs** | **int** | Specifies the timestamp in microseconds when this file was last modified. | [optional] 
**path** | **str** | Specifies the infected file path. | [optional] 
**root_inode_id** | **int** | Specifies the root inode id of the file system which the infected file belongs to. | 
**scanned_time_usecs** | **int** | Specifies the timestamp in microseconds when inode was scanned for viruses. | [optional] 
**state** | **str** | Specifies the state of the infected file. | [optional] 
**threat_descriptions** | **List[str]** | Specifies a list of virus threat descriptions found in the file. | [optional] 
**view_id** | **int** | Specifies the view id which the infected file belongs to. | 
**view_name** | **str** | Specifies the View name to which the infected file belongs to. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.infected_file import InfectedFile

# TODO update the JSON string below
json = "{}"
# create an instance of InfectedFile from a JSON string
infected_file_instance = InfectedFile.from_json(json)
# print the JSON string representation of the object
print(InfectedFile.to_json())

# convert the object into a dict
infected_file_dict = infected_file_instance.to_dict()
# create an instance of InfectedFile from a dict
infected_file_from_dict = InfectedFile.from_dict(infected_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


