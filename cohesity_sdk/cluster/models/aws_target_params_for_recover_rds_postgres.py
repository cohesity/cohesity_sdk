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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.recover_rds_postgres_custom_server_config import RecoverRDSPostgresCustomServerConfig
from cohesity_sdk.cluster.models.recover_rds_postgres_to_known_source_config import RecoverRDSPostgresToKnownSourceConfig
from typing import Set
from typing_extensions import Self

class AwsTargetParamsForRecoverRDSPostgres(BaseModel):
    """
    Specifies the recovery target params for RDS Postgres target config.
    """ # noqa: E501
    custom_server_config: Optional[RecoverRDSPostgresCustomServerConfig] = Field(default=None, alias="customServerConfig")
    known_source_config: Optional[RecoverRDSPostgresToKnownSourceConfig] = Field(default=None, alias="knownSourceConfig")
    recover_to_known_source: Optional[StrictBool] = Field(description="Specifies whether the recovery should be performed to a known or a custom target.", alias="recoverToKnownSource")
    __properties: ClassVar[List[str]] = ["customServerConfig", "knownSourceConfig", "recoverToKnownSource"]

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
        """Create an instance of AwsTargetParamsForRecoverRDSPostgres from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of custom_server_config
        if self.custom_server_config:
            _dict['customServerConfig'] = self.custom_server_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of known_source_config
        if self.known_source_config:
            _dict['knownSourceConfig'] = self.known_source_config.to_dict()
        # set to None if recover_to_known_source (nullable) is None
        # and model_fields_set contains the field
        if self.recover_to_known_source is None and "recover_to_known_source" in self.model_fields_set:
            _dict['recoverToKnownSource'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AwsTargetParamsForRecoverRDSPostgres from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customServerConfig": RecoverRDSPostgresCustomServerConfig.from_dict(obj["customServerConfig"]) if obj.get("customServerConfig") is not None else None,
            "knownSourceConfig": RecoverRDSPostgresToKnownSourceConfig.from_dict(obj["knownSourceConfig"]) if obj.get("knownSourceConfig") is not None else None,
            "recoverToKnownSource": obj.get("recoverToKnownSource")
        })
        return _obj


