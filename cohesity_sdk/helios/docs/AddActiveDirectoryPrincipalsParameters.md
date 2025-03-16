# AddActiveDirectoryPrincipalsParameters

Specifies the parameters for adding Active Directory users and groups to the Cohesity Cluster. You cannot create users and groups in the default Cohesity domain called 'LOCAL' using this operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies a description about the user or group. | [optional] 
**domain_name** | **str** | Specifies the domain of the Active Directory where the referenced principal is stored. | 
**name** | **str** | Specifies the name of the Active Directory principal, that will be referenced by the group or user. The name of the Active Directory principal is used for naming the new group or user on the Cohesity Cluster. | 
**object_class** | **str** | Specifies the type of Active Directory principal.&lt;br&gt; &#39;User&#39; specifies a user object class.&lt;br&gt; &#39;Group&#39; specifies a group object class.&lt;br&gt; &#39;ServiceAccount&#39; specifies a service account object class. | 
**restricted** | **bool** | Whether the principal is a restricted principal. A restricted principal can only view the objects he has permissions to. | [optional] 
**roles** | **List[str]** | Specifies the Cohesity roles to associate with this user or group such as &#39;Admin&#39;, &#39;Ops&#39; or &#39;View&#39;. The Cohesity roles determine privileges on the Cohesity Cluster for this group or user. For example if the &#39;joe&#39; user is added form the Active Directory and is associated with the Cohesity &#39;View&#39; role,&#39;joe&#39; can log in to the Cohesity Dashboard and has a read-only view of the data on the Cohesity Cluster. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.add_active_directory_principals_parameters import AddActiveDirectoryPrincipalsParameters

# TODO update the JSON string below
json = "{}"
# create an instance of AddActiveDirectoryPrincipalsParameters from a JSON string
add_active_directory_principals_parameters_instance = AddActiveDirectoryPrincipalsParameters.from_json(json)
# print the JSON string representation of the object
print(AddActiveDirectoryPrincipalsParameters.to_json())

# convert the object into a dict
add_active_directory_principals_parameters_dict = add_active_directory_principals_parameters_instance.to_dict()
# create an instance of AddActiveDirectoryPrincipalsParameters from a dict
add_active_directory_principals_parameters_from_dict = AddActiveDirectoryPrincipalsParameters.from_dict(add_active_directory_principals_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


