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
from cohesity_sdk.helios.models.recover_exchange_app_params import RecoverExchangeAppParams
from cohesity_sdk.helios.models.recover_exchange_dbs_params import RecoverExchangeDbsParams
from typing import Set
from typing_extensions import Self

class RecoverExchangeParams(BaseModel):
    """
    Specifies the recovery options specific to Exchange environment.
    """ # noqa: E501
    recover_app_params: Optional[RecoverExchangeAppParams] = Field(default=None, description="Specifies the parameters to recover Exchange databases using SMB share.", alias="recoverAppParams")
    recover_exchange_dbs_params: Optional[RecoverExchangeDbsParams] = Field(default=None, description="Specifies the parameters to recover Exchange databases.", alias="recoverExchangeDbsParams")
    recovery_action: StrictStr = Field(description="Specifies the type of recover action to be performed.", alias="recoveryAction")
    __properties: ClassVar[List[str]] = ["recoverAppParams", "recoverExchangeDbsParams", "recoveryAction"]

    @field_validator('recovery_action')
    def recovery_action_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['RecoverApps', 'RecoverExchangeDbs']):
            raise ValueError("must be one of enum values ('RecoverApps', 'RecoverExchangeDbs')")
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
        """Create an instance of RecoverExchangeParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of recover_app_params
        if self.recover_app_params:
            _dict['recoverAppParams'] = self.recover_app_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recover_exchange_dbs_params
        if self.recover_exchange_dbs_params:
            _dict['recoverExchangeDbsParams'] = self.recover_exchange_dbs_params.to_dict()
        # set to None if recover_app_params (nullable) is None
        # and model_fields_set contains the field
        if self.recover_app_params is None and "recover_app_params" in self.model_fields_set:
            _dict['recoverAppParams'] = None

        # set to None if recover_exchange_dbs_params (nullable) is None
        # and model_fields_set contains the field
        if self.recover_exchange_dbs_params is None and "recover_exchange_dbs_params" in self.model_fields_set:
            _dict['recoverExchangeDbsParams'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverExchangeParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "recoverAppParams": RecoverExchangeAppParams.from_dict(obj["recoverAppParams"]) if obj.get("recoverAppParams") is not None else None,
            "recoverExchangeDbsParams": RecoverExchangeDbsParams.from_dict(obj["recoverExchangeDbsParams"]) if obj.get("recoverExchangeDbsParams") is not None else None,
            "recoveryAction": obj.get("recoveryAction")
        })
        return _obj


