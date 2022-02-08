# ProtectionPolicyResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies a unique Policy id assigned by the Cohesity Cluster. | [optional] 
**template_id** | **str, none_type** | Specifies the parent policy template id to which the policy is linked to. This field is set only when policy is created from template. | [optional] 
**is_usable** | **bool, none_type** | This field is set to true if the linked policy which is internally created from a policy templates qualifies as usable to create more policies on the cluster. If the linked policy is partially filled and can not create a working policy then this field will be set to false. In case of normal policy created on the cluster, this field wont be populated. | [optional] 
**is_replicated** | **bool, none_type** | This field is set to true when policy is the replicated policy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


