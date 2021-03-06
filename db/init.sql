\c Piece_de_tache

CREATE TABLE IF NOT EXISTS public.piece
(
    "id_Piece" integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    nom_piece text COLLATE pg_catalog."default" NOT NULL,
    prix_piece real NOT NULL,
    CONSTRAINT piece_pkey PRIMARY KEY ("id_Piece")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.piece
    OWNER to postgres;