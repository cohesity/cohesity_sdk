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
from typing import Optional, Set
from typing_extensions import Self

class SupportMfaConfigInfo(BaseModel):
    """
    Holds the MFA configuration to be returned or stored.
    """ # noqa: E501
    email: Optional[StrictStr] = Field(default=None, description="Specifies email address of the support user. Used when MFA mode is email.")
    enabled: Optional[StrictBool] = Field(default=False, description="Specifies whether MFA is enabled for support user.")
    mfa_code: Optional[StrictStr] = Field(default=None, description="MFA code that needs to be passed when disabling MFA or changing email address when email based MFA is configured.", alias="mfaCode")
    mfa_type: Optional[StrictStr] = Field(default=None, description="Specifies the mechanism to receive the OTP code.", alias="mfaType")
    otp_verification_state: Optional[StrictStr] = Field(default=None, description="Specifies the status of otp verification.", alias="otpVerificationState")
    __properties: ClassVar[List[str]] = ["email", "enabled", "mfaCode", "mfaType", "otpVerificationState"]

    @field_validator('mfa_type')
    def mfa_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['email', 'totp', 'salesforce']):
            raise ValueError("must be one of enum values ('email', 'totp', 'salesforce')")
        return value

    @field_validator('otp_verification_state')
    def otp_verification_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kNotStarted', 'kSuccess', 'kFailure', 'kPending']):
            raise ValueError("must be one of enum values ('kNotStarted', 'kSuccess', 'kFailure', 'kPending')")
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
        """Create an instance of SupportMfaConfigInfo from a JSON string"""
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
        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if mfa_code (nullable) is None
        # and model_fields_set contains the field
        if self.mfa_code is None and "mfa_code" in self.model_fields_set:
            _dict['mfaCode'] = None

        # set to None if mfa_type (nullable) is None
        # and model_fields_set contains the field
        if self.mfa_type is None and "mfa_type" in self.model_fields_set:
            _dict['mfaType'] = None

        # set to None if otp_verification_state (nullable) is None
        # and model_fields_set contains the field
        if self.otp_verification_state is None and "otp_verification_state" in self.model_fields_set:
            _dict['otpVerificationState'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SupportMfaConfigInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else False,
            "mfaCode": obj.get("mfaCode"),
            "mfaType": obj.get("mfaType"),
            "otpVerificationState": obj.get("otpVerificationState")
        })
        return _obj


