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
from cohesity_sdk.helios.models.local_user_response_params import LocalUserResponseParams
from cohesity_sdk.helios.models.s3_account_params import S3AccountParams
from typing import Set
from typing_extensions import Self

class UserParams(BaseModel):
    """
    Specifies a User.
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Specifies the description of the User.")
    effective_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the epoch time in milliseconds since when the user can login.", alias="effectiveTimeMsecs")
    expiry_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the epoch time in milliseconds when the user expires. Post expiry the user cannot access Cohesity cluster.", alias="expiryTimeMsecs")
    locked: Optional[StrictBool] = Field(default=None, description="Specifies whether the User is locked.")
    restricted: Optional[StrictBool] = Field(default=None, description="Specifies whether the User is restricted. A restricted user can only view & manage the objects it has permissions to.")
    roles: Optional[List[StrictStr]] = Field(default=None, description="Specifies the Cohesity roles to associate with the user. The Cohesity roles determine privileges on the Cohesity Cluster for this user.")
    created_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the epoch time in milliseconds when the user account was created.", alias="createdTimeMsecs")
    domain: Optional[StrictStr] = Field(default=None, description="Specifies the domain of the user. For active directories, this is the fully qualified domain name (FQDN). It is 'LOCAL' for local users on the Cohesity Cluster. A user is uniquely identified by combination of the username and the domain.")
    force_password_change: Optional[StrictBool] = Field(default=None, description="Specifies if the user must change password.", alias="forcePasswordChange")
    last_login_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the epoch time in milliseconds when the user last logged in successfully.", alias="lastLoginTimeMsecs")
    last_updated_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the epoch time in milliseconds when the user account was last modified.", alias="lastUpdatedTimeMsecs")
    local_user_params: Optional[LocalUserResponseParams] = Field(default=None, alias="localUserParams")
    locked_reason: Optional[StrictStr] = Field(default=None, description="Specifies the reason for locking the User.", alias="lockedReason")
    other_groups: Optional[List[StrictStr]] = Field(default=None, description="Specifies additional groups the User may belong to.", alias="otherGroups")
    primary_group: Optional[StrictStr] = Field(default=None, description="Specifies the primary group of the User. Primary group is used for file access.", alias="primaryGroup")
    s3_account_params: Optional[S3AccountParams] = Field(default=None, alias="s3AccountParams")
    sid: Optional[StrictStr] = Field(default=None, description="Specifies the sid of the User.")
    tenant_id: Optional[StrictStr] = Field(default=None, description="Specifies the tenant id of the User.", alias="tenantId")
    username: Optional[StrictStr] = Field(default=None, description="Specifies the username.")
    __properties: ClassVar[List[str]] = ["description", "effectiveTimeMsecs", "expiryTimeMsecs", "locked", "restricted", "roles", "createdTimeMsecs", "domain", "forcePasswordChange", "lastLoginTimeMsecs", "lastUpdatedTimeMsecs", "localUserParams", "lockedReason", "otherGroups", "primaryGroup", "s3AccountParams", "sid", "tenantId", "username"]

    @field_validator('locked_reason')
    def locked_reason_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NotLocked', 'FailedLoginAttempts', 'LockedByAdmin', 'Inactivity', 'OtherReasons']):
            raise ValueError("must be one of enum values ('NotLocked', 'FailedLoginAttempts', 'LockedByAdmin', 'Inactivity', 'OtherReasons')")
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
        """Create an instance of UserParams from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_time_msecs",
            "domain",
            "force_password_change",
            "last_login_time_msecs",
            "last_updated_time_msecs",
            "locked_reason",
            "other_groups",
            "primary_group",
            "sid",
            "username",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of local_user_params
        if self.local_user_params:
            _dict['localUserParams'] = self.local_user_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of s3_account_params
        if self.s3_account_params:
            _dict['s3AccountParams'] = self.s3_account_params.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if effective_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.effective_time_msecs is None and "effective_time_msecs" in self.model_fields_set:
            _dict['effectiveTimeMsecs'] = None

        # set to None if expiry_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.expiry_time_msecs is None and "expiry_time_msecs" in self.model_fields_set:
            _dict['expiryTimeMsecs'] = None

        # set to None if locked (nullable) is None
        # and model_fields_set contains the field
        if self.locked is None and "locked" in self.model_fields_set:
            _dict['locked'] = None

        # set to None if restricted (nullable) is None
        # and model_fields_set contains the field
        if self.restricted is None and "restricted" in self.model_fields_set:
            _dict['restricted'] = None

        # set to None if roles (nullable) is None
        # and model_fields_set contains the field
        if self.roles is None and "roles" in self.model_fields_set:
            _dict['roles'] = None

        # set to None if created_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.created_time_msecs is None and "created_time_msecs" in self.model_fields_set:
            _dict['createdTimeMsecs'] = None

        # set to None if force_password_change (nullable) is None
        # and model_fields_set contains the field
        if self.force_password_change is None and "force_password_change" in self.model_fields_set:
            _dict['forcePasswordChange'] = None

        # set to None if last_login_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.last_login_time_msecs is None and "last_login_time_msecs" in self.model_fields_set:
            _dict['lastLoginTimeMsecs'] = None

        # set to None if last_updated_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.last_updated_time_msecs is None and "last_updated_time_msecs" in self.model_fields_set:
            _dict['lastUpdatedTimeMsecs'] = None

        # set to None if locked_reason (nullable) is None
        # and model_fields_set contains the field
        if self.locked_reason is None and "locked_reason" in self.model_fields_set:
            _dict['lockedReason'] = None

        # set to None if primary_group (nullable) is None
        # and model_fields_set contains the field
        if self.primary_group is None and "primary_group" in self.model_fields_set:
            _dict['primaryGroup'] = None

        # set to None if sid (nullable) is None
        # and model_fields_set contains the field
        if self.sid is None and "sid" in self.model_fields_set:
            _dict['sid'] = None

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenantId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "effectiveTimeMsecs": obj.get("effectiveTimeMsecs"),
            "expiryTimeMsecs": obj.get("expiryTimeMsecs"),
            "locked": obj.get("locked"),
            "restricted": obj.get("restricted"),
            "roles": obj.get("roles"),
            "createdTimeMsecs": obj.get("createdTimeMsecs"),
            "domain": obj.get("domain"),
            "forcePasswordChange": obj.get("forcePasswordChange"),
            "lastLoginTimeMsecs": obj.get("lastLoginTimeMsecs"),
            "lastUpdatedTimeMsecs": obj.get("lastUpdatedTimeMsecs"),
            "localUserParams": LocalUserResponseParams.from_dict(obj["localUserParams"]) if obj.get("localUserParams") is not None else None,
            "lockedReason": obj.get("lockedReason"),
            "otherGroups": obj.get("otherGroups"),
            "primaryGroup": obj.get("primaryGroup"),
            "s3AccountParams": S3AccountParams.from_dict(obj["s3AccountParams"]) if obj.get("s3AccountParams") is not None else None,
            "sid": obj.get("sid"),
            "tenantId": obj.get("tenantId"),
            "username": obj.get("username")
        })
        return _obj


