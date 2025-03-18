# GroupParams

Specifies a Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies the description of the group. | [optional] 
**domain** | **str** | Specifies the domain of the group. For active directories, this is the fully qualified domain name (FQDN). It is &#39;LOCAL&#39; for local groups on the Cohesity Cluster. A group is uniquely identified by combination of the name and the domain. | 
**local_group_params** | [**LocalGroupParams**](LocalGroupParams.md) |  | [optional] 
**name** | **str** | Specifies the name of the group. | 
**restricted** | **bool** | Specifies whether the Group is restricted. A restricted group can only view &amp; manage the objects it has permissions to. | [optional] 
**roles** | **List[str]** | Specifies the Cohesity roles to associate with the group. The Cohesity roles determine privileges on the Cohesity Cluster for this group. | [optional] 
**tenant_ids** | **List[str]** | Specifies a list of tenant ids who can access this group. | [optional] 
**created_time_msecs** | **int** | Specifies the epoch time in milliseconds when the group was created. | [optional] [readonly] 
**last_updated_time_msecs** | **int** | Specifies the epoch time in milliseconds when the group was last modified. | [optional] [readonly] 
**sid** | **str** | Specifies the sid of the Group. | [optional] [readonly] 
**smb_principals** | [**List[SMBPrincipal]**](SMBPrincipal.md) | Specifies the SMB principals. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.group_params import GroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of GroupParams from a JSON string
group_params_instance = GroupParams.from_json(json)
# print the JSON string representation of the object
print(GroupParams.to_json())

# convert the object into a dict
group_params_dict = group_params_instance.to_dict()
# create an instance of GroupParams from a dict
group_params_from_dict = GroupParams.from_dict(group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


