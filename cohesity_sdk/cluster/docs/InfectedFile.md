# InfectedFile

Specifes an infected file.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str, none_type** | Specifies the infected file path. | [optional] 
**entity_id** | **int, none_type** | Specifies the entity id of the infected file. | [optional] 
**root_inode_id** | **int, none_type** | Specifies the root inode id of the file system which the infected file belongs to. | [optional] 
**view_id** | **int, none_type** | Specifies the view id which the infected file belongs to. | [optional] 
**state** | **str, none_type** | Sepcifies the state of the infected file. | [optional] 
**threat_descriptions** | **[str], none_type** | Specifies a list of virus threat descriptions found in the file. | [optional] 
**scanned_time_usecs** | **int, none_type** | Specifies the timestamp in microseconds when inode was scanned for viruses. | [optional] 
**detected_time_usecs** | **int, none_type** | Specifies the timestamp in microseconds when the threats were detected. | [optional] 
**last_modified_time_usecs** | **int, none_type** | Specifies the timestamp in microseconds when this file was last modified. | [optional] 
**antivirus_service_icap_uri** | **str, none_type** | Specifies the ICAP Uri of the Antivirus Service which detected the threats. | [optional] 
**antivirus_service_group_name** | **str, none_type** | Specifies the Antivirus Service group which detected the threats. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


