# CreateGroupParams

Specifies the parameters to create a new Cohesity Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Specifies the domain of the group. For active directories, this is the fully qualified domain name (FQDN). It is &#39;LOCAL&#39; for local groups on the Cohesity Cluster. A group is uniquely identified by combination of the name and the domain. | 
**name** | **str** | Specifies the name of the group. | 
**description** | **str, none_type** | Specifies the description of the group. | [optional] 
**local_group_params** | [**LocalGroupParams**](LocalGroupParams.md) |  | [optional] 
**restricted** | **bool, none_type** | Specifies whether the Group is restricted. A restricted group can only view &amp; manage the objects it has permissions to. | [optional] 
**roles** | **[str]** | Specifies the Cohesity roles to associate with the group. The Cohesity roles determine privileges on the Cohesity Cluster for this group. | [optional] 
**tenant_ids** | **[str]** | Specifies a list of tenant ids who can access this group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


