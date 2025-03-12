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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.construct_meta_info_sfdc_params import ConstructMetaInfoSfdcParams
from cohesity_sdk.cluster.models.construct_restore_meta_info_oracle_params import ConstructRestoreMetaInfoOracleParams
from typing import Set
from typing_extensions import Self

class ConstructMetaInfoRequest(BaseModel):
    """
    Params to construct meta info
    """ # noqa: E501
    environment: Optional[StrictStr] = Field(description="Specifies the environment type of the Protection group")
    oracle_params: Optional[ConstructRestoreMetaInfoOracleParams] = Field(default=None, alias="oracleParams")
    sfdc_params: Optional[ConstructMetaInfoSfdcParams] = Field(default=None, alias="sfdcParams")
    __properties: ClassVar[List[str]] = ["environment", "oracleParams", "sfdcParams"]

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
        """Create an instance of ConstructMetaInfoRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of oracle_params
        if self.oracle_params:
            _dict['oracleParams'] = self.oracle_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sfdc_params
        if self.sfdc_params:
            _dict['sfdcParams'] = self.sfdc_params.to_dict()
        # set to None if environment (nullable) is None
        # and model_fields_set contains the field
        if self.environment is None and "environment" in self.model_fields_set:
            _dict['environment'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConstructMetaInfoRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "environment": obj.get("environment"),
            "oracleParams": ConstructRestoreMetaInfoOracleParams.from_dict(obj["oracleParams"]) if obj.get("oracleParams") is not None else None,
            "sfdcParams": ConstructMetaInfoSfdcParams.from_dict(obj["sfdcParams"]) if obj.get("sfdcParams") is not None else None
        })
        return _obj


