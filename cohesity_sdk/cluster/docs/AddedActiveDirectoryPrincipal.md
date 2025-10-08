# AddedActiveDirectoryPrincipal

Specifies a group or user added to the Cohesity Cluster for an Active Directory principal.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str, none_type** | Specifies the domain of the Active Directory where the referenced principal is stored. | 
**name** | **str, none_type** | Specifies the name of the Active Directory principal, that will be referenced by the group or user. The name of the Active Directory principal is used for naming the new group or user on the Cohesity Cluster. | 
**object_class** | **str, none_type** | Specifies the type of Active Directory principal.&lt;br&gt; &#39;User&#39; specifies a user object class.&lt;br&gt; &#39;Group&#39; specifies a group object class.&lt;br&gt; &#39;ServiceAccount&#39; specifies a service account object class. | 
**description** | **str, none_type** | Specifies a description about the user or group. | [optional] 
**restricted** | **bool, none_type** | Whether the principal is a restricted principal. A restricted principal can only view the objects he has permissions to. | [optional] 
**roles** | **[str], none_type** | Specifies the Cohesity roles to associate with this user or group such as &#39;Admin&#39;, &#39;Ops&#39; or &#39;View&#39;. The Cohesity roles determine privileges on the Cohesity Cluster for this group or user. For example if the &#39;joe&#39; user is added form the Active Directory and is associated with the Cohesity &#39;View&#39; role,&#39;joe&#39; can log in to the Cohesity Dashboard and has a read-only view of the data on the Cohesity Cluster. | [optional] 
**created_time_msecs** | **int, none_type** | Specifies the epoch time in milliseconds when the group or user was added to the Cohesity Cluster. | [optional] 
**last_updated_time_msecs** | **int, none_type** | Specifies the epoch time in milliseconds when the group or user was last modified on the Cohesity Cluster. | [optional] 
**sid** | **str, none_type** | Specifies the unique Security ID (SID) of the Active Directory principal associated with this group or user. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


