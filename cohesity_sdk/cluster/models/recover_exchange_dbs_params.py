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
from cohesity_sdk.cluster.models.exchange_target_params_for_recover_exchange_dbs import ExchangeTargetParamsForRecoverExchangeDbs
from typing import Set
from typing_extensions import Self

class RecoverExchangeDbsParams(BaseModel):
    """
    Specifies the parameters to recover Exchange databases.
    """ # noqa: E501
    exchange_target_params: Optional[ExchangeTargetParamsForRecoverExchangeDbs] = Field(default=None, alias="exchangeTargetParams")
    recover_to_new_source: StrictBool = Field(description="Specifies the parameter whether the recovery should be performed to a new or an existing target.", alias="recoverToNewSource")
    target_environment: StrictStr = Field(description="Specifies the environment of the recovery target. The corresponding params below must be filled out.", alias="targetEnvironment")
    __properties: ClassVar[List[str]] = ["exchangeTargetParams", "recoverToNewSource", "targetEnvironment"]

    @field_validator('target_environment')
    def target_environment_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['kExchange']):
            raise ValueError("must be one of enum values ('kExchange')")
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
        """Create an instance of RecoverExchangeDbsParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of exchange_target_params
        if self.exchange_target_params:
            _dict['exchangeTargetParams'] = self.exchange_target_params.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverExchangeDbsParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "exchangeTargetParams": ExchangeTargetParamsForRecoverExchangeDbs.from_dict(obj["exchangeTargetParams"]) if obj.get("exchangeTargetParams") is not None else None,
            "recoverToNewSource": obj.get("recoverToNewSource"),
            "targetEnvironment": obj.get("targetEnvironment")
        })
        return _obj


