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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.common_recover_object_snapshot_params import CommonRecoverObjectSnapshotParams
from cohesity_sdk.helios.models.mailbox_param import MailboxParam
from cohesity_sdk.helios.models.one_drive_param import OneDriveParam
from typing import Set
from typing_extensions import Self

class MsGroupParam(BaseModel):
    """
    Specifies parameters to recover MS group.
    """ # noqa: E501
    mailbox_restore_params: Optional[MailboxParam] = Field(default=None, alias="mailboxRestoreParams")
    mailbox_restore_type: Optional[StrictStr] = Field(default=None, description="Specifies whether mailbox restore is full or granular.", alias="mailboxRestoreType")
    recover_entire_group: Optional[StrictBool] = Field(default=None, description="Specifies if the entire Group (mailbox + site) is to be restored.", alias="recoverEntireGroup")
    recover_object: CommonRecoverObjectSnapshotParams = Field(alias="recoverObject")
    site_restore_params: Optional[List[OneDriveParam]] = Field(default=None, description="Specifies the parameters to recover a MSGroup site document.", alias="siteRestoreParams")
    site_restore_type: Optional[StrictStr] = Field(default=None, description="Specifies whether site restore is full or granular.", alias="siteRestoreType")
    __properties: ClassVar[List[str]] = ["mailboxRestoreParams", "mailboxRestoreType", "recoverEntireGroup", "recoverObject", "siteRestoreParams", "siteRestoreType"]

    @field_validator('mailbox_restore_type')
    def mailbox_restore_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kFull', 'kPartial']):
            raise ValueError("must be one of enum values ('kFull', 'kPartial')")
        return value

    @field_validator('site_restore_type')
    def site_restore_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kFull', 'kPartial']):
            raise ValueError("must be one of enum values ('kFull', 'kPartial')")
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
        """Create an instance of MsGroupParam from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of mailbox_restore_params
        if self.mailbox_restore_params:
            _dict['mailboxRestoreParams'] = self.mailbox_restore_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recover_object
        if self.recover_object:
            _dict['recoverObject'] = self.recover_object.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in site_restore_params (list)
        _items = []
        if self.site_restore_params:
            for _item_site_restore_params in self.site_restore_params:
                if _item_site_restore_params:
                    _items.append(_item_site_restore_params.to_dict())
            _dict['siteRestoreParams'] = _items
        # set to None if mailbox_restore_type (nullable) is None
        # and model_fields_set contains the field
        if self.mailbox_restore_type is None and "mailbox_restore_type" in self.model_fields_set:
            _dict['mailboxRestoreType'] = None

        # set to None if recover_entire_group (nullable) is None
        # and model_fields_set contains the field
        if self.recover_entire_group is None and "recover_entire_group" in self.model_fields_set:
            _dict['recoverEntireGroup'] = None

        # set to None if site_restore_params (nullable) is None
        # and model_fields_set contains the field
        if self.site_restore_params is None and "site_restore_params" in self.model_fields_set:
            _dict['siteRestoreParams'] = None

        # set to None if site_restore_type (nullable) is None
        # and model_fields_set contains the field
        if self.site_restore_type is None and "site_restore_type" in self.model_fields_set:
            _dict['siteRestoreType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MsGroupParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mailboxRestoreParams": MailboxParam.from_dict(obj["mailboxRestoreParams"]) if obj.get("mailboxRestoreParams") is not None else None,
            "mailboxRestoreType": obj.get("mailboxRestoreType"),
            "recoverEntireGroup": obj.get("recoverEntireGroup"),
            "recoverObject": CommonRecoverObjectSnapshotParams.from_dict(obj["recoverObject"]) if obj.get("recoverObject") is not None else None,
            "siteRestoreParams": [OneDriveParam.from_dict(_item) for _item in obj["siteRestoreParams"]] if obj.get("siteRestoreParams") is not None else None,
            "siteRestoreType": obj.get("siteRestoreType")
        })
        return _obj


