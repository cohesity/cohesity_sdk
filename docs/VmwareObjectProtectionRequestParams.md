# VmwareObjectProtectionRequestParams

Specifies the parameters which are specific to VMware object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_consistent_snapshot** | **bool** | Specifies whether or not to quiesce apps and the file system in order to take app consistent snapshots. | [optional] 
**enable_nbdssl_fallback** | **bool** | If this field is set to true and SAN transport backup fails, then backup will fallback to use NBDSSL transport. This field only applies if &#39;leverageSanTransport&#39; is set to true. | [optional] 
**fallback_to_crash_consistent_snapshot** | **bool** | Specifies whether or not to fallback to a crash consistent snapshot in the event that an app consistent snapshot fails. This parameter defaults to true and only changes the behavior of the operation if &#39;appConsistentSnapshot&#39; is set to &#39;true&#39;. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**leverage_san_transport** | **bool** | If this field is set to true, then the backup for the objects will be performed using dedicated storage area network (SAN) instead of LAN or managment network. | [optional] 
**pre_post_script** | [**PrePostScriptParams**](PrePostScriptParams.md) |  | [optional] 
**skip_physical_rdm_disks** | **bool** | Specifies whether or not to skip backing up physical RDM disks. Physical RDM disks cannot be backed up, so if you attempt to backup a VM with physical RDM disks and this value is set to &#39;false&#39;, then those VM backups will fail. | [optional] 
**global_exclude_disks** | [**List[DiskInfo]**](DiskInfo.md) | Specifies a list of disks to exclude from the backup. | [optional] 
**objects** | [**List[VmwareObjectProtectionRequest]**](VmwareObjectProtectionRequest.md) | Specifies the objects to include in the backup. | 

## Example

```python
from cohesity_sdk.cluster.models.vmware_object_protection_request_params import VmwareObjectProtectionRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareObjectProtectionRequestParams from a JSON string
vmware_object_protection_request_params_instance = VmwareObjectProtectionRequestParams.from_json(json)
# print the JSON string representation of the object
print(VmwareObjectProtectionRequestParams.to_json())

# convert the object into a dict
vmware_object_protection_request_params_dict = vmware_object_protection_request_params_instance.to_dict()
# create an instance of VmwareObjectProtectionRequestParams from a dict
vmware_object_protection_request_params_from_dict = VmwareObjectProtectionRequestParams.from_dict(vmware_object_protection_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


