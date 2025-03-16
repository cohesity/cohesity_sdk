# VmwareProtectionGroupExtraParams

Specifies the extra parameters which are specific to VMware object protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_parallel_runs** | **bool** | Specifies whether or not this job can have parallel runs. | [optional] 
**cloud_migration** | **bool** | Specifies whether or not to move the workload to the cloud. | [optional] 
**exclude_filters** | [**List[VMFilter]**](VMFilter.md) | Specifies the list of exclusion filters applied during the group creation or edit. These exclusion filters can be wildcard supported strings or regular expressions. Objects satisfying these filters will be excluded during backup and also auto protected objects will be ignored if filtered by any of the filters. | [optional] 
**exclude_object_ids** | **List[Optional[int]]** | Specifies the list of IDs of the objects to not be protected in this backup. This field only applies if provided object id is non leaf entity such as Tag or a folder. This can be used to ignore specific objects under a parent object which has been included for protection. | [optional] 
**exclude_vm_tag_ids** | **List[List[int]]** | Array of Arrays of VM Tag Ids that Specify VMs to Exclude. Optionally specify a list of VMs to exclude from protecting by listing Protection Source ids of VM Tags in this two dimensional array. Using this two dimensional array of Tag ids, the Cluster generates a list of VMs to exclude from protecting, which are derived from intersections of the inner arrays and union of the outer array, as shown by the following example. For example a Datacenter is selected to be protected but you want to exclude all the &#39;Former Employees&#39; VMs in the East and West but keep all the VMs for &#39;Former Employees&#39; in the South which are also stored in this Datacenter, by specifying the following tag id array: [ [1000, 2221], [1000, 3031] ], where 1000 is the &#39;Former Employee&#39; VM Tag id, 2221 is the &#39;East&#39; VM Tag id and 3031 is the &#39;West&#39; VM Tag id. The first inner array [1000, 2221] produces a list of VMs that are both tagged with &#39;Former Employees&#39; and &#39;East&#39; (an intersection). The second inner array [1000, 3031] produces a list of VMs that are both tagged with &#39;Former Employees&#39; and &#39;West&#39; (an intersection). The outer array combines the list of VMs from the two inner arrays. The list of resulting VMs are excluded from being protected this Job. | [optional] 
**leverage_hyperflex_snapshots** | **bool** | Whether to leverage the hyperflex based snapshots for this backup. To leverage hyperflex snapshots, it has to first be registered. If hyperflex based snapshots cannot be taken, backup will fallback to the default backup method. | [optional] 
**leverage_nutanix_snapshots** | **bool** | Whether to leverage the nutanix based snapshots for this backup. To leverage nutanix snapshots, it has to first be registered. If nutanix based snapshots cannot be taken, backup will fallback to the default backup method. | [optional] 
**leverage_storage_snapshots** | **bool** | Whether to leverage the storage array based snapshots for this backup. To leverage storage snapshots, the storage array has to be registered as a source. If storage based snapshots can not be taken, backup will fallback to the default backup method. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**vm_tag_ids** | **List[List[int]]** | Array of Array of VM Tag Ids that Specify VMs to Protect. Optionally specify a list of VMs to protect by listing Protection Source ids of VM Tags in this two dimensional array. Using this two dimensional array of Tag ids, the Cluster generates a list of VMs to protect which are derived from intersections of the inner arrays and union of the outer array, as shown by the following example. To protect only &#39;Eng&#39; VMs in the East and all the VMs in the West, specify the following tag id array: [ [1101, 2221], [3031] ], where 1101 is the &#39;Eng&#39; VM Tag id, 2221 is the &#39;East&#39; VM Tag id and 3031 is the &#39;West&#39; VM Tag id. The inner array [1101, 2221] produces a list of VMs that are both tagged with &#39;Eng&#39; and &#39;East&#39; (an intersection). The outer array combines the list from the inner array with list of VMs tagged with &#39;West&#39; (a union). The list of resulting VMs are protected by this Protection Group. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.vmware_protection_group_extra_params import VmwareProtectionGroupExtraParams

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareProtectionGroupExtraParams from a JSON string
vmware_protection_group_extra_params_instance = VmwareProtectionGroupExtraParams.from_json(json)
# print the JSON string representation of the object
print(VmwareProtectionGroupExtraParams.to_json())

# convert the object into a dict
vmware_protection_group_extra_params_dict = vmware_protection_group_extra_params_instance.to_dict()
# create an instance of VmwareProtectionGroupExtraParams from a dict
vmware_protection_group_extra_params_from_dict = VmwareProtectionGroupExtraParams.from_dict(vmware_protection_group_extra_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


