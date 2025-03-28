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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class UsersDiscoveryParams(BaseModel):
    """
    Specifies discovery params for User(mailbox/onedrive) entities. It should only be populated when the 'DiscoveryParams.discoverableObjectTypeList' includes 'kUsers' otherwise this will be ignored.
    """ # noqa: E501
    allow_chats_backup: Optional[StrictBool] = Field(default=None, description="Specifies whether users' chats should be backed up or not. If this is false or not specified users' chats backup will not be done.", alias="allowChatsBackup")
    discover_users_with_mailbox: Optional[StrictBool] = Field(default=None, description="Specifies if office 365 users with valid mailboxes should be discovered or not.", alias="discoverUsersWithMailbox")
    discover_users_with_onedrive: Optional[StrictBool] = Field(default=None, description="Specifies if office 365 users with valid Onedrives should be discovered or not.", alias="discoverUsersWithOnedrive")
    fetch_mailbox_info: Optional[StrictBool] = Field(default=None, description="Specifies whether users' mailbox info including the provisioning status, mailbox type & in-place archival support will be fetched and processed.", alias="fetchMailboxInfo")
    fetch_one_drive_info: Optional[StrictBool] = Field(default=None, description="Specifies whether users' onedrive info including the provisioning status & storage quota will be fetched and processed.", alias="fetchOneDriveInfo")
    skip_users_without_my_site: Optional[StrictBool] = Field(default=None, description="Specifies whether to skip processing user who have uninitialized OneDrive or are without MySite.", alias="skipUsersWithoutMySite")
    __properties: ClassVar[List[str]] = ["allowChatsBackup", "discoverUsersWithMailbox", "discoverUsersWithOnedrive", "fetchMailboxInfo", "fetchOneDriveInfo", "skipUsersWithoutMySite"]

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
        """Create an instance of UsersDiscoveryParams from a JSON string"""
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
        # set to None if allow_chats_backup (nullable) is None
        # and model_fields_set contains the field
        if self.allow_chats_backup is None and "allow_chats_backup" in self.model_fields_set:
            _dict['allowChatsBackup'] = None

        # set to None if discover_users_with_mailbox (nullable) is None
        # and model_fields_set contains the field
        if self.discover_users_with_mailbox is None and "discover_users_with_mailbox" in self.model_fields_set:
            _dict['discoverUsersWithMailbox'] = None

        # set to None if discover_users_with_onedrive (nullable) is None
        # and model_fields_set contains the field
        if self.discover_users_with_onedrive is None and "discover_users_with_onedrive" in self.model_fields_set:
            _dict['discoverUsersWithOnedrive'] = None

        # set to None if fetch_mailbox_info (nullable) is None
        # and model_fields_set contains the field
        if self.fetch_mailbox_info is None and "fetch_mailbox_info" in self.model_fields_set:
            _dict['fetchMailboxInfo'] = None

        # set to None if fetch_one_drive_info (nullable) is None
        # and model_fields_set contains the field
        if self.fetch_one_drive_info is None and "fetch_one_drive_info" in self.model_fields_set:
            _dict['fetchOneDriveInfo'] = None

        # set to None if skip_users_without_my_site (nullable) is None
        # and model_fields_set contains the field
        if self.skip_users_without_my_site is None and "skip_users_without_my_site" in self.model_fields_set:
            _dict['skipUsersWithoutMySite'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UsersDiscoveryParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowChatsBackup": obj.get("allowChatsBackup"),
            "discoverUsersWithMailbox": obj.get("discoverUsersWithMailbox"),
            "discoverUsersWithOnedrive": obj.get("discoverUsersWithOnedrive"),
            "fetchMailboxInfo": obj.get("fetchMailboxInfo"),
            "fetchOneDriveInfo": obj.get("fetchOneDriveInfo"),
            "skipUsersWithoutMySite": obj.get("skipUsersWithoutMySite")
        })
        return _obj


