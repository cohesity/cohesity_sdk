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
from cohesity_sdk.helios.models.oracle_pdb_restore_params import OraclePdbRestoreParams
from typing import Set
from typing_extensions import Self

class RecoverOracleGranularRestoreInfo(BaseModel):
    """
    Specifies information about list of objects (PDBs) to restore.
    """ # noqa: E501
    granularity_type: Optional[StrictStr] = Field(default=None, description="Specifies type of granular restore.", alias="granularityType")
    pdb_restore_params: Optional[OraclePdbRestoreParams] = Field(default=None, alias="pdbRestoreParams")
    __properties: ClassVar[List[str]] = ["granularityType", "pdbRestoreParams"]

    @field_validator('granularity_type')
    def granularity_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kPDB']):
            raise ValueError("must be one of enum values ('kPDB')")
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
        """Create an instance of RecoverOracleGranularRestoreInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pdb_restore_params
        if self.pdb_restore_params:
            _dict['pdbRestoreParams'] = self.pdb_restore_params.to_dict()
        # set to None if granularity_type (nullable) is None
        # and model_fields_set contains the field
        if self.granularity_type is None and "granularity_type" in self.model_fields_set:
            _dict['granularityType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverOracleGranularRestoreInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "granularityType": obj.get("granularityType"),
            "pdbRestoreParams": OraclePdbRestoreParams.from_dict(obj["pdbRestoreParams"]) if obj.get("pdbRestoreParams") is not None else None
        })
        return _obj


