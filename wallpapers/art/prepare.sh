#!/usr/bin/env bash
# Copy the raw Midjourney drops from ai-prompts/ into art/ under clean names,
# as declared in manifest.mjs. Idempotent.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$HERE/../ai-prompts"

copy() { cp -f "$SRC/$1" "$HERE/$2"; echo "  $2"; }

echo "==> Preparing art/"
copy "u4858417731__A_quiet_residential_courtyard_at_blue_hour_warm__2c7b08c3-c0da-4021-9b07-d9ab6d4ea2dc_2.png" courtyard.png
copy "u4858417731__Abstract_aerial_view_of_a_small_neighborhood_at__f318c4b6-8c5e-4efe-84a9-e8a8ea81b3e1_3.png" aerial.png
copy "u4858417731__Minimal_abstract_background_soft_flowing_bands_o_c5060090-5a1d-4c1b-b7ba-35a56c29e32a_3.png" bands.png
copy "u4858417731__A_softly_lit_rooftop_terrace_at_dusk_two_empty_c_c3ce91e5-b202-4ef2-bff2-557ce99dd41a_2.png" terrace.png
copy "u4858417731__Elegant_topographic_contour_lines_of_a_city_dist_de26da6b-9882-4fa8-9806-331f2bb3abb7_2.png" contour.png
copy "u4858417731__Two_warmly_lit_apartment_windows_facing_each_oth_7894e22c-6cb1-4165-a2e4-e090bd6a373e_0.png" windows.png
copy "u4858417731__Minimal_warm_off-white_concrete_texture_e9e6dd_s_c40a4544-2d53-4546-aa39-408e9f04faba_0.png" arc.png
copy "u4858417731_Facade_of_warm_cream_apartment_building_in_soft_m_1b98570b-fc20-4ca8-b064-745d4184d1cf_0.png" facade.png
copy "u4858417731__Abstract_minimal_composition_of_soft_dissolving__1f98618e-2a21-42f7-8ff1-296a80b5a1b7_2.png" dust.png
echo "==> Done"
