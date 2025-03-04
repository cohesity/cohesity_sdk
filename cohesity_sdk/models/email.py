# coding: utf-8

"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.models.object_summary import ObjectSummary
from cohesity_sdk.models.snapshot_tag_info import SnapshotTagInfo
from cohesity_sdk.models.tag_info import TagInfo
from typing import Optional, Set
from typing_extensions import Self

class Email(BaseModel):
    """
    Specifies an email or an email folder.
    """ # noqa: E501
    snapshot_tags: Optional[List[SnapshotTagInfo]] = Field(default=None, description="Specifies snapshot tags applied to the object.", alias="snapshotTags")
    tags: Optional[List[TagInfo]] = Field(default=None, description="Specifies tag applied to the object.")
    bcc_recipient_addresses: Optional[List[StrictStr]] = Field(default=None, description="\"Specifies the email addresses of all the BCC receipients of this email.\"", alias="bccRecipientAddresses")
    cc_recipient_addresses: Optional[List[StrictStr]] = Field(default=None, description="\"Specifies the email addresses of all the CC receipients of this email.\"", alias="ccRecipientAddresses")
    created_time_secs: Optional[StrictInt] = Field(default=None, description="\"Specifies the Unix timestamp epoch in seconds at which this item is created.\"", alias="createdTimeSecs")
    directory_path: Optional[StrictStr] = Field(default=None, description="Specifies the directory path to this mailbox item.", alias="directoryPath")
    email_addresses: Optional[List[StrictStr]] = Field(default=None, description="Specifies the email addresses of a contact.", alias="emailAddresses")
    email_subject: Optional[StrictStr] = Field(default=None, description="Specifies the subject of this email.", alias="emailSubject")
    first_name: Optional[StrictStr] = Field(default=None, description="Specifies the contact's first name.", alias="firstName")
    folder_name: Optional[StrictStr] = Field(default=None, description="Specify the name of the email folder.", alias="folderName")
    has_attachment: Optional[StrictBool] = Field(default=None, description="Specifies whether email has an attachment.", alias="hasAttachment")
    id: Optional[StrictStr] = Field(default=None, description="Specifies the id of the email object.")
    last_modification_name: Optional[StrictStr] = Field(default=None, description="\"Specifies the name of the person who modified this item.\"", alias="lastModificationName")
    last_modification_time_secs: Optional[StrictInt] = Field(default=None, description="\"Specifies the Unix timestamp epoch in seconds at which this item was modified.\"", alias="lastModificationTimeSecs")
    last_name: Optional[StrictStr] = Field(default=None, description="Specifies the contact's last name.", alias="lastName")
    optional_attendees_addresses: Optional[List[StrictStr]] = Field(default=None, description="\"Specifies the email addresses of all the optional attendees of this calendar item.\"", alias="optionalAttendeesAddresses")
    organizer_address: Optional[StrictStr] = Field(default=None, description="\"Specifies the calendar item organizer's email address.\"", alias="organizerAddress")
    parent_folder_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of parent folder the mailbox item.", alias="parentFolderId")
    path: Optional[StrictStr] = Field(default=None, description="Specifies the path to this mailbox item.")
    protection_group_id: Optional[StrictStr] = Field(default=None, description="\"Specifies the Protection Group id protecting the mailbox.\"", alias="protectionGroupId")
    protection_group_name: Optional[StrictStr] = Field(default=None, description="\"Specifies the Protection Group name protecting the mailbox item.\"", alias="protectionGroupName")
    received_time_secs: Optional[StrictInt] = Field(default=None, description="\"Specifies the Unix timestamp epoch in seconds at which this email is received.\"", alias="receivedTimeSecs")
    recipient_addresses: Optional[List[StrictStr]] = Field(default=None, description="\"Specifies the email addresses of all receipients of this email.\"", alias="recipientAddresses")
    required_attendees_addresses: Optional[List[StrictStr]] = Field(default=None, description="\"Specifies the email addresses of all required attendees of this calendar item.\"", alias="requiredAttendeesAddresses")
    sender_address: Optional[StrictStr] = Field(default=None, description="Specifies the sender's email address.", alias="senderAddress")
    sent_time_secs: Optional[StrictInt] = Field(default=None, description="\"Specifies the Unix timestamp epoch in seconds at which this email is sent.\"", alias="sentTimeSecs")
    storage_domain_id: Optional[StrictInt] = Field(default=None, description="\"Specifies the Storage Domain id where the backup data of Object is present.\"", alias="storageDomainId")
    task_completion_date_time_secs: Optional[StrictInt] = Field(default=None, description="\"Specifies the Unix timestamp epoch in seconds at which this task item was completed.\"", alias="taskCompletionDateTimeSecs")
    task_due_date_time_secs: Optional[StrictInt] = Field(default=None, description="\"Specifies the Unix timestamp epoch in seconds at which this task item is due.\"", alias="taskDueDateTimeSecs")
    task_status: Optional[StrictStr] = Field(default=None, description="Specifies the task item status type.", alias="taskStatus")
    tenant_id: Optional[StrictStr] = Field(default=None, description="\"Specify the tenant id to which this email belongs to.\"", alias="tenantId")
    type: Optional[StrictStr] = Field(default=None, description="Specifies the Mailbox item type.")
    user_object_info: Optional[ObjectSummary] = Field(default=None, alias="userObjectInfo")
    __properties: ClassVar[List[str]] = ["snapshotTags", "tags", "bccRecipientAddresses", "ccRecipientAddresses", "createdTimeSecs", "directoryPath", "emailAddresses", "emailSubject", "firstName", "folderName", "hasAttachment", "id", "lastModificationName", "lastModificationTimeSecs", "lastName", "optionalAttendeesAddresses", "organizerAddress", "parentFolderId", "path", "protectionGroupId", "protectionGroupName", "receivedTimeSecs", "recipientAddresses", "requiredAttendeesAddresses", "senderAddress", "sentTimeSecs", "storageDomainId", "taskCompletionDateTimeSecs", "taskDueDateTimeSecs", "taskStatus", "tenantId", "type", "userObjectInfo"]

    @field_validator('task_status')
    def task_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NotStarted', 'InProgress', 'Completed', 'WaitingOnOthers', 'Deferred']):
            raise ValueError("must be one of enum values ('NotStarted', 'InProgress', 'Completed', 'WaitingOnOthers', 'Deferred')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Email', 'Folder', 'Calendar', 'Contact', 'Task', 'Note']):
            raise ValueError("must be one of enum values ('Email', 'Folder', 'Calendar', 'Contact', 'Task', 'Note')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Email from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in snapshot_tags (list)
        _items = []
        if self.snapshot_tags:
            for _item_snapshot_tags in self.snapshot_tags:
                if _item_snapshot_tags:
                    _items.append(_item_snapshot_tags.to_dict())
            _dict['snapshotTags'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item_tags in self.tags:
                if _item_tags:
                    _items.append(_item_tags.to_dict())
            _dict['tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of user_object_info
        if self.user_object_info:
            _dict['userObjectInfo'] = self.user_object_info.to_dict()
        # set to None if snapshot_tags (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_tags is None and "snapshot_tags" in self.model_fields_set:
            _dict['snapshotTags'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if bcc_recipient_addresses (nullable) is None
        # and model_fields_set contains the field
        if self.bcc_recipient_addresses is None and "bcc_recipient_addresses" in self.model_fields_set:
            _dict['bccRecipientAddresses'] = None

        # set to None if cc_recipient_addresses (nullable) is None
        # and model_fields_set contains the field
        if self.cc_recipient_addresses is None and "cc_recipient_addresses" in self.model_fields_set:
            _dict['ccRecipientAddresses'] = None

        # set to None if created_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.created_time_secs is None and "created_time_secs" in self.model_fields_set:
            _dict['createdTimeSecs'] = None

        # set to None if directory_path (nullable) is None
        # and model_fields_set contains the field
        if self.directory_path is None and "directory_path" in self.model_fields_set:
            _dict['directoryPath'] = None

        # set to None if email_addresses (nullable) is None
        # and model_fields_set contains the field
        if self.email_addresses is None and "email_addresses" in self.model_fields_set:
            _dict['emailAddresses'] = None

        # set to None if email_subject (nullable) is None
        # and model_fields_set contains the field
        if self.email_subject is None and "email_subject" in self.model_fields_set:
            _dict['emailSubject'] = None

        # set to None if first_name (nullable) is None
        # and model_fields_set contains the field
        if self.first_name is None and "first_name" in self.model_fields_set:
            _dict['firstName'] = None

        # set to None if folder_name (nullable) is None
        # and model_fields_set contains the field
        if self.folder_name is None and "folder_name" in self.model_fields_set:
            _dict['folderName'] = None

        # set to None if has_attachment (nullable) is None
        # and model_fields_set contains the field
        if self.has_attachment is None and "has_attachment" in self.model_fields_set:
            _dict['hasAttachment'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if last_modification_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_modification_name is None and "last_modification_name" in self.model_fields_set:
            _dict['lastModificationName'] = None

        # set to None if last_modification_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.last_modification_time_secs is None and "last_modification_time_secs" in self.model_fields_set:
            _dict['lastModificationTimeSecs'] = None

        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['lastName'] = None

        # set to None if optional_attendees_addresses (nullable) is None
        # and model_fields_set contains the field
        if self.optional_attendees_addresses is None and "optional_attendees_addresses" in self.model_fields_set:
            _dict['optionalAttendeesAddresses'] = None

        # set to None if organizer_address (nullable) is None
        # and model_fields_set contains the field
        if self.organizer_address is None and "organizer_address" in self.model_fields_set:
            _dict['organizerAddress'] = None

        # set to None if parent_folder_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_folder_id is None and "parent_folder_id" in self.model_fields_set:
            _dict['parentFolderId'] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if protection_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_id is None and "protection_group_id" in self.model_fields_set:
            _dict['protectionGroupId'] = None

        # set to None if protection_group_name (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_name is None and "protection_group_name" in self.model_fields_set:
            _dict['protectionGroupName'] = None

        # set to None if received_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.received_time_secs is None and "received_time_secs" in self.model_fields_set:
            _dict['receivedTimeSecs'] = None

        # set to None if recipient_addresses (nullable) is None
        # and model_fields_set contains the field
        if self.recipient_addresses is None and "recipient_addresses" in self.model_fields_set:
            _dict['recipientAddresses'] = None

        # set to None if required_attendees_addresses (nullable) is None
        # and model_fields_set contains the field
        if self.required_attendees_addresses is None and "required_attendees_addresses" in self.model_fields_set:
            _dict['requiredAttendeesAddresses'] = None

        # set to None if sender_address (nullable) is None
        # and model_fields_set contains the field
        if self.sender_address is None and "sender_address" in self.model_fields_set:
            _dict['senderAddress'] = None

        # set to None if sent_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.sent_time_secs is None and "sent_time_secs" in self.model_fields_set:
            _dict['sentTimeSecs'] = None

        # set to None if storage_domain_id (nullable) is None
        # and model_fields_set contains the field
        if self.storage_domain_id is None and "storage_domain_id" in self.model_fields_set:
            _dict['storageDomainId'] = None

        # set to None if task_completion_date_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.task_completion_date_time_secs is None and "task_completion_date_time_secs" in self.model_fields_set:
            _dict['taskCompletionDateTimeSecs'] = None

        # set to None if task_due_date_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.task_due_date_time_secs is None and "task_due_date_time_secs" in self.model_fields_set:
            _dict['taskDueDateTimeSecs'] = None

        # set to None if task_status (nullable) is None
        # and model_fields_set contains the field
        if self.task_status is None and "task_status" in self.model_fields_set:
            _dict['taskStatus'] = None

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenantId'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Email from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "snapshotTags": [SnapshotTagInfo.from_dict(_item) for _item in obj["snapshotTags"]] if obj.get("snapshotTags") is not None else None,
            "tags": [TagInfo.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "bccRecipientAddresses": obj.get("bccRecipientAddresses"),
            "ccRecipientAddresses": obj.get("ccRecipientAddresses"),
            "createdTimeSecs": obj.get("createdTimeSecs"),
            "directoryPath": obj.get("directoryPath"),
            "emailAddresses": obj.get("emailAddresses"),
            "emailSubject": obj.get("emailSubject"),
            "firstName": obj.get("firstName"),
            "folderName": obj.get("folderName"),
            "hasAttachment": obj.get("hasAttachment"),
            "id": obj.get("id"),
            "lastModificationName": obj.get("lastModificationName"),
            "lastModificationTimeSecs": obj.get("lastModificationTimeSecs"),
            "lastName": obj.get("lastName"),
            "optionalAttendeesAddresses": obj.get("optionalAttendeesAddresses"),
            "organizerAddress": obj.get("organizerAddress"),
            "parentFolderId": obj.get("parentFolderId"),
            "path": obj.get("path"),
            "protectionGroupId": obj.get("protectionGroupId"),
            "protectionGroupName": obj.get("protectionGroupName"),
            "receivedTimeSecs": obj.get("receivedTimeSecs"),
            "recipientAddresses": obj.get("recipientAddresses"),
            "requiredAttendeesAddresses": obj.get("requiredAttendeesAddresses"),
            "senderAddress": obj.get("senderAddress"),
            "sentTimeSecs": obj.get("sentTimeSecs"),
            "storageDomainId": obj.get("storageDomainId"),
            "taskCompletionDateTimeSecs": obj.get("taskCompletionDateTimeSecs"),
            "taskDueDateTimeSecs": obj.get("taskDueDateTimeSecs"),
            "taskStatus": obj.get("taskStatus"),
            "tenantId": obj.get("tenantId"),
            "type": obj.get("type"),
            "userObjectInfo": ObjectSummary.from_dict(obj["userObjectInfo"]) if obj.get("userObjectInfo") is not None else None
        })
        return _obj


