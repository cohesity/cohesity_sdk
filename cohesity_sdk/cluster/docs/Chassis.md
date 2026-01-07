# Chassis

Specifies information about hardware chassis.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_node_base** | **int** | This field is initialized as sum of maximum slots of all the chassis added to the cluster so far plus one. This is required to assign unique node index for the nodes when they are added to the cluster. Please refer to cluster_node_index in Node below. | [optional] 
**hardware_model** | **str, none_type** | Specifies the hardware model of the chassis.Like ivybridge, haswell. | [optional] 
**id** | **int, none_type** | Each chassis in a cluster is assigned a unique id when the chassis is added to the cluster first time. The index starts from 1. The use of an integer id helps speed up internal computations involving chassis. This integer will not change during the lifetime of the chassis in the cluster. | [optional] 
**location** | **str, none_type** | Location of the chassis within the rack. | [optional] 
**name** | **str, none_type** | Unique name assigned to this chassis. This is set to the serial number of the chassis by one of the following two ways. 1) by the chassis manufacturer for non-cohesity systems, and cohesity systems built before jira ticket ECO-2 was approved. 2) by a cohesity contract manufacturer for cohesity systems built after jira ticket ECO-2 was approved. | [optional] 
**node_ids** | **[int], none_type** | Specifies list of ids of all the nodes in chassis. | [optional] 
**rack_id** | **int, none_type** | Rack Id that this chassis belong to | [optional] 
**serial_number** | **str, none_type** | Specifies the serial number of the chassis. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


