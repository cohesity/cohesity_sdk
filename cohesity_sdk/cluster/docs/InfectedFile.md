# InfectedFile

Specifies an infected entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **int, none_type** | Specifies the entity id of the infected entity. | 
**root_inode_id** | **int, none_type** | Specifies the root inode id of the file system which the infected entity belongs to. | 
**view_id** | **int, none_type** | Specifies the view id which the infected entity belongs to. | 
**antivirus_service_group_name** | **str, none_type** | Specifies the Antivirus Service group which detected the threats. | [optional] 
**antivirus_service_icap_uri** | **str, none_type** | Specifies the ICAP Uri of the Antivirus Service which detected the threats. | [optional] 
**detected_time_usecs** | **int, none_type** | Specifies the timestamp in microseconds when the threats were detected. | [optional] 
**entity_type** | **str, none_type** | Specifies the type of the infected entity. | [optional] 
**last_modified_time_usecs** | **int, none_type** | Specifies the timestamp in microseconds when this entity was last modified. | [optional] 
**path** | **str, none_type** | Specifies the infected entity path. | [optional] 
**scanned_time_usecs** | **int, none_type** | Specifies the timestamp in microseconds when inode was scanned for viruses. | [optional] 
**state** | **str, none_type** | Specifies the state of the infected entity. | [optional] 
**threat_descriptions** | **[str], none_type** | Specifies a list of virus threat descriptions found in the entity. | [optional] 
**view_name** | **str, none_type** | Specifies the View name to which the infected entity belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


