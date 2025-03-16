# AddedActiveDirectoryPrincipal

Specifies a group or user added to the Cohesity Cluster for an Active Directory principal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies a description about the user or group. | [optional] 
**domain_name** | **str** | Specifies the domain of the Active Directory where the referenced principal is stored. | 
**name** | **str** | Specifies the name of the Active Directory principal, that will be referenced by the group or user. The name of the Active Directory principal is used for naming the new group or user on the Cohesity Cluster. | 
**object_class** | **str** | Specifies the type of Active Directory principal.&lt;br&gt; &#39;User&#39; specifies a user object class.&lt;br&gt; &#39;Group&#39; specifies a group object class.&lt;br&gt; &#39;ServiceAccount&#39; specifies a service account object class. | 
**restricted** | **bool** | Whether the principal is a restricted principal. A restricted principal can only view the objects he has permissions to. | [optional] 
**roles** | **List[str]** | Specifies the Cohesity roles to associate with this user or group such as &#39;Admin&#39;, &#39;Ops&#39; or &#39;View&#39;. The Cohesity roles determine privileges on the Cohesity Cluster for this group or user. For example if the &#39;joe&#39; user is added form the Active Directory and is associated with the Cohesity &#39;View&#39; role,&#39;joe&#39; can log in to the Cohesity Dashboard and has a read-only view of the data on the Cohesity Cluster. | [optional] 
**created_time_msecs** | **int** | Specifies the epoch time in milliseconds when the group or user was added to the Cohesity Cluster. | [optional] 
**last_updated_time_msecs** | **int** | Specifies the epoch time in milliseconds when the group or user was last modified on the Cohesity Cluster. | [optional] 
**sid** | **str** | Specifies the unique Security ID (SID) of the Active Directory principal associated with this group or user. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.added_active_directory_principal import AddedActiveDirectoryPrincipal

# TODO update the JSON string below
json = "{}"
# create an instance of AddedActiveDirectoryPrincipal from a JSON string
added_active_directory_principal_instance = AddedActiveDirectoryPrincipal.from_json(json)
# print the JSON string representation of the object
print(AddedActiveDirectoryPrincipal.to_json())

# convert the object into a dict
added_active_directory_principal_dict = added_active_directory_principal_instance.to_dict()
# create an instance of AddedActiveDirectoryPrincipal from a dict
added_active_directory_principal_from_dict = AddedActiveDirectoryPrincipal.from_dict(added_active_directory_principal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


