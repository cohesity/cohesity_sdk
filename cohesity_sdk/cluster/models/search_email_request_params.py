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
from cohesity_sdk.cluster.models.o365_search_emails_request_params import O365SearchEmailsRequestParams
from typing import Set
from typing_extensions import Self

class SearchEmailRequestParams(BaseModel):
    """
    Specifies the request parameters to search for emails and email folders.
    """ # noqa: E501
    attendees_addresses: Optional[List[StrictStr]] = Field(default=None, description="Filters the calendar items which have specified email addresses as attendees.", alias="attendeesAddresses")
    bcc_recipient_addresses: Optional[List[StrictStr]] = Field(default=None, description="Filters the emails which are sent to specified email addresses in BCC.", alias="bccRecipientAddresses")
    cc_recipient_addresses: Optional[List[StrictStr]] = Field(default=None, description="Filters the emails which are sent to specified email addresses in CC.", alias="ccRecipientAddresses")
    created_end_time_secs: Optional[StrictInt] = Field(default=None, description="Specifies the end time in Unix timestamp epoch in seconds where the created time of the email/item is less than specified value.", alias="createdEndTimeSecs")
    created_start_time_secs: Optional[StrictInt] = Field(default=None, description="Specifies the start time in Unix timestamp epoch in seconds where the created time of the email/item is more than specified value.", alias="createdStartTimeSecs")
    due_date_end_time_secs: Optional[StrictInt] = Field(default=None, description="Specifies the end time in Unix timestamp epoch in seconds where the last modification time of the email/item is less than specified value.", alias="dueDateEndTimeSecs")
    due_date_start_time_secs: Optional[StrictInt] = Field(default=None, description="Specifies the start time in Unix timestamp epoch in seconds where the last modification time of the email/item is more than specified value.", alias="dueDateStartTimeSecs")
    email_address: Optional[StrictStr] = Field(default=None, description="Filters the contact items which have specified text in email address.", alias="emailAddress")
    email_subject: Optional[StrictStr] = Field(default=None, description="Filters the emails which have the specified text in its subject.", alias="emailSubject")
    first_name: Optional[StrictStr] = Field(default=None, description="Filters the contacts with specified text in first name.", alias="firstName")
    folder_names: Optional[List[StrictStr]] = Field(default=None, description="Filters the emails which are categorized to specified folders.", alias="folderNames")
    has_attachment: Optional[StrictBool] = Field(default=None, description="Filters the emails which have attachment.", alias="hasAttachment")
    last_modified_end_time_secs: Optional[StrictInt] = Field(default=None, description="Specifies the end time in Unix timestamp epoch in seconds where the last modification time of the email/item is less than specified value.", alias="lastModifiedEndTimeSecs")
    last_modified_start_time_secs: Optional[StrictInt] = Field(default=None, description="Specifies the start time in Unix timestamp epoch in seconds where the last modification time of the email/item is more than specified value.", alias="lastModifiedStartTimeSecs")
    last_name: Optional[StrictStr] = Field(default=None, description="Filters the contacts with specified text in last name.", alias="lastName")
    middle_name: Optional[StrictStr] = Field(default=None, description="Filters the contacts with specified text in middle name.", alias="middleName")
    organizer_address: Optional[StrictStr] = Field(default=None, description="Filters the calendar items which are organized by specified User's email address.", alias="organizerAddress")
    received_end_time_secs: Optional[StrictInt] = Field(default=None, description="Specifies the end time in Unix timestamp epoch in seconds where the received time of the email is less than specified value.", alias="receivedEndTimeSecs")
    received_start_time_secs: Optional[StrictInt] = Field(default=None, description="Specifies the start time in Unix timestamp epoch in seconds where the received time of the email is more than specified value.", alias="receivedStartTimeSecs")
    recipient_addresses: Optional[List[StrictStr]] = Field(default=None, description="Filters the emails which are sent to specified email addresses.", alias="recipientAddresses")
    sender_address: Optional[StrictStr] = Field(default=None, description="Filters the emails which are received from specified User's email address.", alias="senderAddress")
    source_environment: Optional[StrictStr] = Field(default=None, description="Specifies the source environment.", alias="sourceEnvironment")
    task_status_types: Optional[List[StrictStr]] = Field(default=None, description="Specifies a list of task item status types. Task items having status within the given types will be returned.", alias="taskStatusTypes")
    types: Optional[List[StrictStr]] = Field(default=None, description="Specifies a list of mailbox item types. Only items within the given types will be returned.")
    o365_params: Optional[O365SearchEmailsRequestParams] = Field(default=None, alias="o365Params")
    __properties: ClassVar[List[str]] = ["attendeesAddresses", "bccRecipientAddresses", "ccRecipientAddresses", "createdEndTimeSecs", "createdStartTimeSecs", "dueDateEndTimeSecs", "dueDateStartTimeSecs", "emailAddress", "emailSubject", "firstName", "folderNames", "hasAttachment", "lastModifiedEndTimeSecs", "lastModifiedStartTimeSecs", "lastName", "middleName", "organizerAddress", "receivedEndTimeSecs", "receivedStartTimeSecs", "recipientAddresses", "senderAddress", "sourceEnvironment", "taskStatusTypes", "types", "o365Params"]

    @field_validator('source_environment')
    def source_environment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kO365']):
            raise ValueError("must be one of enum values ('kO365')")
        return value

    @field_validator('task_status_types')
    def task_status_types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['NotStarted', 'InProgress', 'Completed', 'WaitingOnOthers', 'Deferred']):
                raise ValueError("each list item must be one of ('NotStarted', 'InProgress', 'Completed', 'WaitingOnOthers', 'Deferred')")
        return value

    @field_validator('types')
    def types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['Email', 'Folder', 'Calendar', 'Contact', 'Task', 'Note']):
                raise ValueError("each list item must be one of ('Email', 'Folder', 'Calendar', 'Contact', 'Task', 'Note')")
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
        """Create an instance of SearchEmailRequestParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of o365_params
        if self.o365_params:
            _dict['o365Params'] = self.o365_params.to_dict()
        # set to None if attendees_addresses (nullable) is None
        # and model_fields_set contains the field
        if self.attendees_addresses is None and "attendees_addresses" in self.model_fields_set:
            _dict['attendeesAddresses'] = None

        # set to None if bcc_recipient_addresses (nullable) is None
        # and model_fields_set contains the field
        if self.bcc_recipient_addresses is None and "bcc_recipient_addresses" in self.model_fields_set:
            _dict['bccRecipientAddresses'] = None

        # set to None if cc_recipient_addresses (nullable) is None
        # and model_fields_set contains the field
        if self.cc_recipient_addresses is None and "cc_recipient_addresses" in self.model_fields_set:
            _dict['ccRecipientAddresses'] = None

        # set to None if created_end_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.created_end_time_secs is None and "created_end_time_secs" in self.model_fields_set:
            _dict['createdEndTimeSecs'] = None

        # set to None if created_start_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.created_start_time_secs is None and "created_start_time_secs" in self.model_fields_set:
            _dict['createdStartTimeSecs'] = None

        # set to None if due_date_end_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.due_date_end_time_secs is None and "due_date_end_time_secs" in self.model_fields_set:
            _dict['dueDateEndTimeSecs'] = None

        # set to None if due_date_start_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.due_date_start_time_secs is None and "due_date_start_time_secs" in self.model_fields_set:
            _dict['dueDateStartTimeSecs'] = None

        # set to None if email_address (nullable) is None
        # and model_fields_set contains the field
        if self.email_address is None and "email_address" in self.model_fields_set:
            _dict['emailAddress'] = None

        # set to None if email_subject (nullable) is None
        # and model_fields_set contains the field
        if self.email_subject is None and "email_subject" in self.model_fields_set:
            _dict['emailSubject'] = None

        # set to None if first_name (nullable) is None
        # and model_fields_set contains the field
        if self.first_name is None and "first_name" in self.model_fields_set:
            _dict['firstName'] = None

        # set to None if folder_names (nullable) is None
        # and model_fields_set contains the field
        if self.folder_names is None and "folder_names" in self.model_fields_set:
            _dict['folderNames'] = None

        # set to None if has_attachment (nullable) is None
        # and model_fields_set contains the field
        if self.has_attachment is None and "has_attachment" in self.model_fields_set:
            _dict['hasAttachment'] = None

        # set to None if last_modified_end_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified_end_time_secs is None and "last_modified_end_time_secs" in self.model_fields_set:
            _dict['lastModifiedEndTimeSecs'] = None

        # set to None if last_modified_start_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified_start_time_secs is None and "last_modified_start_time_secs" in self.model_fields_set:
            _dict['lastModifiedStartTimeSecs'] = None

        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['lastName'] = None

        # set to None if middle_name (nullable) is None
        # and model_fields_set contains the field
        if self.middle_name is None and "middle_name" in self.model_fields_set:
            _dict['middleName'] = None

        # set to None if organizer_address (nullable) is None
        # and model_fields_set contains the field
        if self.organizer_address is None and "organizer_address" in self.model_fields_set:
            _dict['organizerAddress'] = None

        # set to None if received_end_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.received_end_time_secs is None and "received_end_time_secs" in self.model_fields_set:
            _dict['receivedEndTimeSecs'] = None

        # set to None if received_start_time_secs (nullable) is None
        # and model_fields_set contains the field
        if self.received_start_time_secs is None and "received_start_time_secs" in self.model_fields_set:
            _dict['receivedStartTimeSecs'] = None

        # set to None if recipient_addresses (nullable) is None
        # and model_fields_set contains the field
        if self.recipient_addresses is None and "recipient_addresses" in self.model_fields_set:
            _dict['recipientAddresses'] = None

        # set to None if sender_address (nullable) is None
        # and model_fields_set contains the field
        if self.sender_address is None and "sender_address" in self.model_fields_set:
            _dict['senderAddress'] = None

        # set to None if source_environment (nullable) is None
        # and model_fields_set contains the field
        if self.source_environment is None and "source_environment" in self.model_fields_set:
            _dict['sourceEnvironment'] = None

        # set to None if task_status_types (nullable) is None
        # and model_fields_set contains the field
        if self.task_status_types is None and "task_status_types" in self.model_fields_set:
            _dict['taskStatusTypes'] = None

        # set to None if types (nullable) is None
        # and model_fields_set contains the field
        if self.types is None and "types" in self.model_fields_set:
            _dict['types'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchEmailRequestParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attendeesAddresses": obj.get("attendeesAddresses"),
            "bccRecipientAddresses": obj.get("bccRecipientAddresses"),
            "ccRecipientAddresses": obj.get("ccRecipientAddresses"),
            "createdEndTimeSecs": obj.get("createdEndTimeSecs"),
            "createdStartTimeSecs": obj.get("createdStartTimeSecs"),
            "dueDateEndTimeSecs": obj.get("dueDateEndTimeSecs"),
            "dueDateStartTimeSecs": obj.get("dueDateStartTimeSecs"),
            "emailAddress": obj.get("emailAddress"),
            "emailSubject": obj.get("emailSubject"),
            "firstName": obj.get("firstName"),
            "folderNames": obj.get("folderNames"),
            "hasAttachment": obj.get("hasAttachment"),
            "lastModifiedEndTimeSecs": obj.get("lastModifiedEndTimeSecs"),
            "lastModifiedStartTimeSecs": obj.get("lastModifiedStartTimeSecs"),
            "lastName": obj.get("lastName"),
            "middleName": obj.get("middleName"),
            "organizerAddress": obj.get("organizerAddress"),
            "receivedEndTimeSecs": obj.get("receivedEndTimeSecs"),
            "receivedStartTimeSecs": obj.get("receivedStartTimeSecs"),
            "recipientAddresses": obj.get("recipientAddresses"),
            "senderAddress": obj.get("senderAddress"),
            "sourceEnvironment": obj.get("sourceEnvironment"),
            "taskStatusTypes": obj.get("taskStatusTypes"),
            "types": obj.get("types"),
            "o365Params": O365SearchEmailsRequestParams.from_dict(obj["o365Params"]) if obj.get("o365Params") is not None else None
        })
        return _obj


