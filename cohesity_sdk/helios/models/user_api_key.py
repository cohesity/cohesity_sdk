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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class UserAPIKey(BaseModel):
    """
    Specifies a user API key instance.
    """ # noqa: E501
    created_by_user_sid: Optional[StrictStr] = Field(default=None, description="Specifies the user SID who created the API key.", alias="createdByUserSid")
    created_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the time in milliseconds when the API key was created.", alias="createdTimeMsecs")
    expiry_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the time in milliseconds when the API key will expire. null signifies no-expiry.", alias="expiryTimeMsecs")
    id: Optional[StrictStr] = Field(default=None, description="Specifies the unique id of the API key.")
    is_active: Optional[StrictBool] = Field(default=True, description="Specifies if the API key is active.", alias="isActive")
    is_expired: Optional[StrictBool] = Field(default=None, description="Specifies if the API key has expired.", alias="isExpired")
    last_rotated_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the time in milliseconds when the API key was last rotated.", alias="lastRotatedTimeMsecs")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the API key name.")
    user_sid: Optional[StrictStr] = Field(default=None, description="Specifies the user who owns the API key.", alias="userSid")
    __properties: ClassVar[List[str]] = ["createdByUserSid", "createdTimeMsecs", "expiryTimeMsecs", "id", "isActive", "isExpired", "lastRotatedTimeMsecs", "name", "userSid"]

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
        """Create an instance of UserAPIKey from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_by_user_sid",
            "created_time_msecs",
            "expiry_time_msecs",
            "id",
            "is_active",
            "is_expired",
            "last_rotated_time_msecs",
            "name",
            "user_sid",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if created_by_user_sid (nullable) is None
        # and model_fields_set contains the field
        if self.created_by_user_sid is None and "created_by_user_sid" in self.model_fields_set:
            _dict['createdByUserSid'] = None

        # set to None if created_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.created_time_msecs is None and "created_time_msecs" in self.model_fields_set:
            _dict['createdTimeMsecs'] = None

        # set to None if expiry_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.expiry_time_msecs is None and "expiry_time_msecs" in self.model_fields_set:
            _dict['expiryTimeMsecs'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if is_active (nullable) is None
        # and model_fields_set contains the field
        if self.is_active is None and "is_active" in self.model_fields_set:
            _dict['isActive'] = None

        # set to None if is_expired (nullable) is None
        # and model_fields_set contains the field
        if self.is_expired is None and "is_expired" in self.model_fields_set:
            _dict['isExpired'] = None

        # set to None if last_rotated_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.last_rotated_time_msecs is None and "last_rotated_time_msecs" in self.model_fields_set:
            _dict['lastRotatedTimeMsecs'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if user_sid (nullable) is None
        # and model_fields_set contains the field
        if self.user_sid is None and "user_sid" in self.model_fields_set:
            _dict['userSid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserAPIKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdByUserSid": obj.get("createdByUserSid"),
            "createdTimeMsecs": obj.get("createdTimeMsecs"),
            "expiryTimeMsecs": obj.get("expiryTimeMsecs"),
            "id": obj.get("id"),
            "isActive": obj.get("isActive") if obj.get("isActive") is not None else True,
            "isExpired": obj.get("isExpired"),
            "lastRotatedTimeMsecs": obj.get("lastRotatedTimeMsecs"),
            "name": obj.get("name"),
            "userSid": obj.get("userSid")
        })
        return _obj


