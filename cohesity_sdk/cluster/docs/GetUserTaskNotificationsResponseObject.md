# GetUserTaskNotificationsResponseObject

All the Notification events are generated for a given user. This is used for transferring notifications over wire using bulk Install agent app.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_list** | [**List[TaskNotification]**](TaskNotification.md) | Specifies the Task Notification list for the given User. | [optional] 
**total_count** | **int** | Specifies the Task Notification Count for the given User. | [optional] 
**unread_count** | **int** | Specifies the Task Notification Unread Count. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.get_user_task_notifications_response_object import GetUserTaskNotificationsResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserTaskNotificationsResponseObject from a JSON string
get_user_task_notifications_response_object_instance = GetUserTaskNotificationsResponseObject.from_json(json)
# print the JSON string representation of the object
print(GetUserTaskNotificationsResponseObject.to_json())

# convert the object into a dict
get_user_task_notifications_response_object_dict = get_user_task_notifications_response_object_instance.to_dict()
# create an instance of GetUserTaskNotificationsResponseObject from a dict
get_user_task_notifications_response_object_from_dict = GetUserTaskNotificationsResponseObject.from_dict(get_user_task_notifications_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


