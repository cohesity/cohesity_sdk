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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.office365_object_protection_common_params import Office365ObjectProtectionCommonParams
from cohesity_sdk.helios.models.office365_sharepoint_site_object_protection_params import Office365SharepointSiteObjectProtectionParams
from cohesity_sdk.helios.models.office365_user_mailbox_object_protection_params import Office365UserMailboxObjectProtectionParams
from cohesity_sdk.helios.models.office365_user_one_drive_object_protection_params import Office365UserOneDriveObjectProtectionParams
from typing import Optional, Set
from typing_extensions import Self

class Office365ObjectProtectionParams(BaseModel):
    """
    Specifies the parameters which are specific to Microsoft 365 Object Protection.
    """ # noqa: E501
    groups_object_protection_params: Optional[Office365ObjectProtectionCommonParams] = Field(default=None, alias="groupsObjectProtectionParams")
    object_protection_type: StrictStr = Field(description="Specifies the Microsoft 365 Object Protection type.", alias="objectProtectionType")
    sharepoint_site_object_protection_params: Optional[Office365SharepointSiteObjectProtectionParams] = Field(default=None, alias="sharepointSiteObjectProtectionParams")
    teams_object_protection_params: Optional[Office365ObjectProtectionCommonParams] = Field(default=None, alias="teamsObjectProtectionParams")
    user_mailbox_object_protection_params: Optional[Office365UserMailboxObjectProtectionParams] = Field(default=None, alias="userMailboxObjectProtectionParams")
    user_one_drive_object_protection_params: Optional[Office365UserOneDriveObjectProtectionParams] = Field(default=None, alias="userOneDriveObjectProtectionParams")
    __properties: ClassVar[List[str]] = ["groupsObjectProtectionParams", "objectProtectionType", "sharepointSiteObjectProtectionParams", "teamsObjectProtectionParams", "userMailboxObjectProtectionParams", "userOneDriveObjectProtectionParams"]

    @field_validator('object_protection_type')
    def object_protection_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['kMailbox', 'kOneDrive', 'kSharePoint', 'kPublicFolders', 'kGroups', 'kTeams']):
            raise ValueError("must be one of enum values ('kMailbox', 'kOneDrive', 'kSharePoint', 'kPublicFolders', 'kGroups', 'kTeams')")
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
        """Create an instance of Office365ObjectProtectionParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of groups_object_protection_params
        if self.groups_object_protection_params:
            _dict['groupsObjectProtectionParams'] = self.groups_object_protection_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sharepoint_site_object_protection_params
        if self.sharepoint_site_object_protection_params:
            _dict['sharepointSiteObjectProtectionParams'] = self.sharepoint_site_object_protection_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of teams_object_protection_params
        if self.teams_object_protection_params:
            _dict['teamsObjectProtectionParams'] = self.teams_object_protection_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_mailbox_object_protection_params
        if self.user_mailbox_object_protection_params:
            _dict['userMailboxObjectProtectionParams'] = self.user_mailbox_object_protection_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_one_drive_object_protection_params
        if self.user_one_drive_object_protection_params:
            _dict['userOneDriveObjectProtectionParams'] = self.user_one_drive_object_protection_params.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Office365ObjectProtectionParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "groupsObjectProtectionParams": Office365ObjectProtectionCommonParams.from_dict(obj["groupsObjectProtectionParams"]) if obj.get("groupsObjectProtectionParams") is not None else None,
            "objectProtectionType": obj.get("objectProtectionType"),
            "sharepointSiteObjectProtectionParams": Office365SharepointSiteObjectProtectionParams.from_dict(obj["sharepointSiteObjectProtectionParams"]) if obj.get("sharepointSiteObjectProtectionParams") is not None else None,
            "teamsObjectProtectionParams": Office365ObjectProtectionCommonParams.from_dict(obj["teamsObjectProtectionParams"]) if obj.get("teamsObjectProtectionParams") is not None else None,
            "userMailboxObjectProtectionParams": Office365UserMailboxObjectProtectionParams.from_dict(obj["userMailboxObjectProtectionParams"]) if obj.get("userMailboxObjectProtectionParams") is not None else None,
            "userOneDriveObjectProtectionParams": Office365UserOneDriveObjectProtectionParams.from_dict(obj["userOneDriveObjectProtectionParams"]) if obj.get("userOneDriveObjectProtectionParams") is not None else None
        })
        return _obj


