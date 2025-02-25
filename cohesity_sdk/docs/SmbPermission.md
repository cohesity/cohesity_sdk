# SmbPermission

Specifies information about a single SMB permission.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **str, none_type** | Specifies the read/write access to the SMB share. &#39;ReadyOnly&#39; indicates read only access to the SMB share. &#39;ReadWrite&#39; indicates read and write access to the SMB share. &#39;FullControl&#39; indicates full administrative control of the SMB share. &#39;SpecialAccess&#39; indicates custom permissions to the SMB share using  access masks structures. &#39;SuperUser&#39; indicates root permissions ignoring all SMB ACLs. | [optional] 
**mode** | **str, none_type** | Specifies how the permission should be applied to folders and/or files. &#39;FolderSubFoldersAndFiles&#39; indicates that permissions are applied to a Folder and it&#39;s sub folders and files. &#39;FolderAndSubFolders&#39; indicates that permissions are applied to a Folder and it&#39;s sub folders. &#39;FolderAndSubFiles&#39; indicates that permissions are applied to a Folder and it&#39;s sub files. &#39;FolderOnly&#39; indicates that permsission are applied to folder only. &#39;SubFoldersAndFilesOnly&#39; indicates that permissions are applied to sub folders and files only. &#39;SubFoldersOnly&#39; indicates that permissiona are applied to sub folders only. &#39;FilesOnly&#39; indicates that permissions are applied to files only. | [optional] 
**sid** | **str, none_type** | Specifies the security identifier (SID) of the principal. | [optional] 
**special_access_mask** | **int, none_type** | Specifies custom access permissions. When the access mask from the Access Control Entry (ACE) cannot be mapped to one of the enums in &#39;access&#39;, this field is populated with the custom mask derived from the ACE and &#39;access&#39; is set to kSpecialAccess. This is a placeholder for storing an unmapped access permission and should not be set when creating and editing a View. | [optional] 
**special_type** | **int, none_type** | Specifies a custom type. When the type from the Access Control Entry (ACE) cannot be mapped to one of the enums in &#39;type&#39;, this field is populated with the custom type derived from the ACE and &#39;type&#39; is set to kSpecialType. This is a placeholder for storing an unmapped type and should not be set when creating and editing a View. | [optional] 
**type** | **str, none_type** | Specifies the type of permission. &#39;Allow&#39; indicates access is allowed. &#39;Deny&#39; indicates access is denied. &#39;SpecialType&#39; indicates a type defined in the Access Control Entry (ACE) does not map to &#39;Allow&#39; or &#39;Deny&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


