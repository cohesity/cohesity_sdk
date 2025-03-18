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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.cassandra_source_config_params import CassandraSourceConfigParams
from cohesity_sdk.cluster.models.h_base_additional_params import HBaseAdditionalParams
from cohesity_sdk.cluster.models.hdfs_additional_params import HdfsAdditionalParams
from cohesity_sdk.cluster.models.hive_additional_params import HiveAdditionalParams
from cohesity_sdk.cluster.models.mssql_connection_response_params import MssqlConnectionResponseParams
from cohesity_sdk.cluster.models.vmware_additional_params import VmwareAdditionalParams
from typing import Set
from typing_extensions import Self

class SourceConnectionResponseParams(BaseModel):
    """
    Specifies the response from a test connection request.
    """ # noqa: E501
    cassandra_connection_response_params: Optional[CassandraSourceConfigParams] = Field(default=None, alias="cassandraConnectionResponseParams")
    connection_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user.", alias="connectionId")
    environment: Optional[StrictStr] = Field(description="Specifies the environment type of the Protection Source.")
    hbase_connection_response_params: Optional[HBaseAdditionalParams] = Field(default=None, alias="hbaseConnectionResponseParams")
    hdfs_connection_response_params: Optional[HdfsAdditionalParams] = Field(default=None, alias="hdfsConnectionResponseParams")
    hive_connection_response_params: Optional[HiveAdditionalParams] = Field(default=None, alias="hiveConnectionResponseParams")
    mssql_connection_response_params: Optional[MssqlConnectionResponseParams] = Field(default=None, alias="mssqlConnectionResponseParams")
    vmware_connection_response_params: Optional[VmwareAdditionalParams] = Field(default=None, alias="vmwareConnectionResponseParams")
    __properties: ClassVar[List[str]] = ["cassandraConnectionResponseParams", "connectionId", "environment", "hbaseConnectionResponseParams", "hdfsConnectionResponseParams", "hiveConnectionResponseParams", "mssqlConnectionResponseParams", "vmwareConnectionResponseParams"]

    @field_validator('environment')
    def environment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kCassandra', 'kHive', 'kHBase', 'kHdfs', 'kSQL', 'kOracle']):
            raise ValueError("must be one of enum values ('kCassandra', 'kHive', 'kHBase', 'kHdfs', 'kSQL', 'kOracle')")
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
        """Create an instance of SourceConnectionResponseParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cassandra_connection_response_params
        if self.cassandra_connection_response_params:
            _dict['cassandraConnectionResponseParams'] = self.cassandra_connection_response_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hbase_connection_response_params
        if self.hbase_connection_response_params:
            _dict['hbaseConnectionResponseParams'] = self.hbase_connection_response_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hdfs_connection_response_params
        if self.hdfs_connection_response_params:
            _dict['hdfsConnectionResponseParams'] = self.hdfs_connection_response_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hive_connection_response_params
        if self.hive_connection_response_params:
            _dict['hiveConnectionResponseParams'] = self.hive_connection_response_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mssql_connection_response_params
        if self.mssql_connection_response_params:
            _dict['mssqlConnectionResponseParams'] = self.mssql_connection_response_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vmware_connection_response_params
        if self.vmware_connection_response_params:
            _dict['vmwareConnectionResponseParams'] = self.vmware_connection_response_params.to_dict()
        # set to None if connection_id (nullable) is None
        # and model_fields_set contains the field
        if self.connection_id is None and "connection_id" in self.model_fields_set:
            _dict['connectionId'] = None

        # set to None if environment (nullable) is None
        # and model_fields_set contains the field
        if self.environment is None and "environment" in self.model_fields_set:
            _dict['environment'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SourceConnectionResponseParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cassandraConnectionResponseParams": CassandraSourceConfigParams.from_dict(obj["cassandraConnectionResponseParams"]) if obj.get("cassandraConnectionResponseParams") is not None else None,
            "connectionId": obj.get("connectionId"),
            "environment": obj.get("environment"),
            "hbaseConnectionResponseParams": HBaseAdditionalParams.from_dict(obj["hbaseConnectionResponseParams"]) if obj.get("hbaseConnectionResponseParams") is not None else None,
            "hdfsConnectionResponseParams": HdfsAdditionalParams.from_dict(obj["hdfsConnectionResponseParams"]) if obj.get("hdfsConnectionResponseParams") is not None else None,
            "hiveConnectionResponseParams": HiveAdditionalParams.from_dict(obj["hiveConnectionResponseParams"]) if obj.get("hiveConnectionResponseParams") is not None else None,
            "mssqlConnectionResponseParams": MssqlConnectionResponseParams.from_dict(obj["mssqlConnectionResponseParams"]) if obj.get("mssqlConnectionResponseParams") is not None else None,
            "vmwareConnectionResponseParams": VmwareAdditionalParams.from_dict(obj["vmwareConnectionResponseParams"]) if obj.get("vmwareConnectionResponseParams") is not None else None
        })
        return _obj


