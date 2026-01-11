# NodeUpgradeParameters

Parameters for Node Upgrade.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_sw_version** | **str** | Specifies the target software version. The node that the request is sent to will search itself for the specified software package and if that package is found, it will be used for the upgrade.  | 
**node_ids** | **[int], none_type** | Specifies a list of IDs of additional nodes to be upgraded. These must be free Nodes present on the same local network as the Node that the request was sent to. The ID of the Node the request was sent to should not be included in this list. This parameter can only be specified if upgradeAllFreeNodes is not specified.  | [optional] 
**upgrade_all_free_nodes** | **bool, none_type** | Specifies whether or not to attempt to upgrade all free nodes which are currently connected to the same local network as the node that the request was sent to. This parameter can only be specified if nodeIds is not specified.  | [optional] 
**upgrade_self** | **bool, none_type** | Specifies that the node that the request is being sent to should be upgraded. By default, this is set to true.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


