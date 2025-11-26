# NodeDiskLocation

Contains the info of the disk on the cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_id** | **int** | The id of the disk where the data is exported. More information w.r.t the disk(mount_path etc) is found in cluster config. | [optional] 
**expected_mount_path** | **str** | Denotes the mount path of the disk. NOTE: This is only expected as it might change during reboots. | [optional] 
**expected_node_ip** | **str** | Denotes the IP of node on which the disk is mounted. NOTE: This is only expected as it might change during reboots. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


