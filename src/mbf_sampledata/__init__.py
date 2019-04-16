import sys
import pandas as pd
from pathlib import Path

def get_sample_data(fn):
    here = Path(__file__).parent
    return str((here / 'data' / fn).absolute())

def get_sample_path(fn):
    here = Path(__file__).parent
    return (here / 'data' / fn).absolute()



def get_human_22_fake_genome():
    from mbf_genomics.testing import MockGenome
    import gzip

    genes = pd.read_msgpack(
        gzip.GzipFile(get_sample_data(Path("mbf_align/hs_22_genes.msgpack.gz")))
    ).reset_index()
    tr = pd.read_msgpack(
        gzip.GzipFile(get_sample_data(Path("mbf_align/hs_22_transcripts.msgpack.gz")))
    ).reset_index()
    return MockGenome(df_genes=genes, df_transcripts=tr, chr_lengths={"22": 50818468})

def get_Candidatus_carsonella_ruddii_pv(name=None, **kwargs):
    """A FilebasedGenome used by other libraries for their tests"""
    from mbf_genomes import FileBasedGenome
    if name is None:  # pragma: no cover
        name = "Candidatus_carsonella"
    return FileBasedGenome(
        name,
        get_sample_path("mbf_genomes/Candidatus_carsonella_ruddii_pv.ASM1036v1.dna.toplevel.fa.gz"),
        get_sample_path("mbf_genomes/Candidatus_carsonella_ruddii_pv.ASM1036v1.42.gtf.gz"),
        get_sample_path("mbf_genomes/Candidatus_carsonella_ruddii_pv.ASM1036v1.cdna.all.fa.gz"),
        get_sample_path("mbf_genomes/Candidatus_carsonella_ruddii_pv.ASM1036v1.pep.all.fa.gz"),
        **kwargs,
    )
