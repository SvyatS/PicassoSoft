CREATE TABLE public.PoliceOrders (
    OrderId int GENERATED ALWAYS AS IDENTITY,
    CrimeId int NOT NULL,
    OriginalCrimeTypeName varchar(128),
    ReportDate timestamp,
    CallDate timestamp,
    OffenseDate timestamp,
    CallTime time,
    CallDateTime timestamp,
    Disposition varchar(32),
    Address varchar(128),
    City varchar(32),
    State varchar(8),
    AgencyId int,
    AddressType varchar(64),
    CommonLocation varchar(128)
);

