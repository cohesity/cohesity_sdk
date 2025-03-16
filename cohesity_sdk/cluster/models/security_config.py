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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.security_config_account_lockout import SecurityConfigAccountLockout
from cohesity_sdk.cluster.models.security_config_certificate_based_auth import SecurityConfigCertificateBasedAuth
from cohesity_sdk.cluster.models.security_config_data_classification import SecurityConfigDataClassification
from cohesity_sdk.cluster.models.security_config_password_lifetime import SecurityConfigPasswordLifetime
from cohesity_sdk.cluster.models.security_config_password_reuse import SecurityConfigPasswordReuse
from cohesity_sdk.cluster.models.security_config_password_strength import SecurityConfigPasswordStrength
from cohesity_sdk.cluster.models.security_config_session_configuration import SecurityConfigSessionConfiguration
from cohesity_sdk.cluster.models.security_config_ssh_configuration import SecurityConfigSshConfiguration
from typing import Optional, Set
from typing_extensions import Self

class SecurityConfig(BaseModel):
    """
    Specifies the fields of security settings.
    """ # noqa: E501
    account_lockout: Optional[SecurityConfigAccountLockout] = Field(default=None, alias="accountLockout")
    auth_token_timeout_minutes: Optional[StrictInt] = Field(default=None, description="Specifies the authentication token timeout in minutes. Applies both for API based access token and browser login cookie.", alias="authTokenTimeoutMinutes")
    certificate_based_auth: Optional[SecurityConfigCertificateBasedAuth] = Field(default=None, alias="certificateBasedAuth")
    data_classification: Optional[SecurityConfigDataClassification] = Field(default=None, alias="dataClassification")
    inactivity_timeout_m_secs: Optional[StrictInt] = Field(default=None, description="Specifies the UI inactivity timeout in milliseconds. Default value is 30 minutes.", alias="inactivityTimeoutMSecs")
    password_lifetime: Optional[SecurityConfigPasswordLifetime] = Field(default=None, alias="passwordLifetime")
    password_reuse: Optional[SecurityConfigPasswordReuse] = Field(default=None, alias="passwordReuse")
    password_strength: Optional[SecurityConfigPasswordStrength] = Field(default=None, alias="passwordStrength")
    session_configuration: Optional[SecurityConfigSessionConfiguration] = Field(default=None, alias="sessionConfiguration")
    ssh_configuration: Optional[SecurityConfigSshConfiguration] = Field(default=None, alias="sshConfiguration")
    __properties: ClassVar[List[str]] = ["accountLockout", "authTokenTimeoutMinutes", "certificateBasedAuth", "dataClassification", "inactivityTimeoutMSecs", "passwordLifetime", "passwordReuse", "passwordStrength", "sessionConfiguration", "sshConfiguration"]

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
        """Create an instance of SecurityConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account_lockout
        if self.account_lockout:
            _dict['accountLockout'] = self.account_lockout.to_dict()
        # override the default output from pydantic by calling `to_dict()` of certificate_based_auth
        if self.certificate_based_auth:
            _dict['certificateBasedAuth'] = self.certificate_based_auth.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data_classification
        if self.data_classification:
            _dict['dataClassification'] = self.data_classification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of password_lifetime
        if self.password_lifetime:
            _dict['passwordLifetime'] = self.password_lifetime.to_dict()
        # override the default output from pydantic by calling `to_dict()` of password_reuse
        if self.password_reuse:
            _dict['passwordReuse'] = self.password_reuse.to_dict()
        # override the default output from pydantic by calling `to_dict()` of password_strength
        if self.password_strength:
            _dict['passwordStrength'] = self.password_strength.to_dict()
        # override the default output from pydantic by calling `to_dict()` of session_configuration
        if self.session_configuration:
            _dict['sessionConfiguration'] = self.session_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ssh_configuration
        if self.ssh_configuration:
            _dict['sshConfiguration'] = self.ssh_configuration.to_dict()
        # set to None if auth_token_timeout_minutes (nullable) is None
        # and model_fields_set contains the field
        if self.auth_token_timeout_minutes is None and "auth_token_timeout_minutes" in self.model_fields_set:
            _dict['authTokenTimeoutMinutes'] = None

        # set to None if inactivity_timeout_m_secs (nullable) is None
        # and model_fields_set contains the field
        if self.inactivity_timeout_m_secs is None and "inactivity_timeout_m_secs" in self.model_fields_set:
            _dict['inactivityTimeoutMSecs'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SecurityConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountLockout": SecurityConfigAccountLockout.from_dict(obj["accountLockout"]) if obj.get("accountLockout") is not None else None,
            "authTokenTimeoutMinutes": obj.get("authTokenTimeoutMinutes"),
            "certificateBasedAuth": SecurityConfigCertificateBasedAuth.from_dict(obj["certificateBasedAuth"]) if obj.get("certificateBasedAuth") is not None else None,
            "dataClassification": SecurityConfigDataClassification.from_dict(obj["dataClassification"]) if obj.get("dataClassification") is not None else None,
            "inactivityTimeoutMSecs": obj.get("inactivityTimeoutMSecs"),
            "passwordLifetime": SecurityConfigPasswordLifetime.from_dict(obj["passwordLifetime"]) if obj.get("passwordLifetime") is not None else None,
            "passwordReuse": SecurityConfigPasswordReuse.from_dict(obj["passwordReuse"]) if obj.get("passwordReuse") is not None else None,
            "passwordStrength": SecurityConfigPasswordStrength.from_dict(obj["passwordStrength"]) if obj.get("passwordStrength") is not None else None,
            "sessionConfiguration": SecurityConfigSessionConfiguration.from_dict(obj["sessionConfiguration"]) if obj.get("sessionConfiguration") is not None else None,
            "sshConfiguration": SecurityConfigSshConfiguration.from_dict(obj["sshConfiguration"]) if obj.get("sshConfiguration") is not None else None
        })
        return _obj


