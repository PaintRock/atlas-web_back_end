-- Glam rock as main style by longevity
SELECT band_name 
FROM metal_bands
WHERE style = Glam rock
ORDER BY (split - formed) AS lifespan DESC
;