# PerformVaultActionsReq

Parameters to perform actions on a vault.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** | Specifies the action type which is being performed on a FortKnox vault. &lt;br&gt; &#39;Resume&#39; resumes a failed provisioning of FortKnox vault. This action will trigger the provisioning of the given vault again. &lt;br&gt; | 

## Example

```python
from cohesity_sdk.helios.models.perform_vault_actions_req import PerformVaultActionsReq

# TODO update the JSON string below
json = "{}"
# create an instance of PerformVaultActionsReq from a JSON string
perform_vault_actions_req_instance = PerformVaultActionsReq.from_json(json)
# print the JSON string representation of the object
print(PerformVaultActionsReq.to_json())

# convert the object into a dict
perform_vault_actions_req_dict = perform_vault_actions_req_instance.to_dict()
# create an instance of PerformVaultActionsReq from a dict
perform_vault_actions_req_from_dict = PerformVaultActionsReq.from_dict(perform_vault_actions_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


