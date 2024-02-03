-- Glam rock as main style by longevity
SELECT band_name, 
    IFNULL(split, 2024) - formed AS lifespan
FROM metal_bands
WHERE style Like 'Glam rock'
ORDER BY lifespan DESC
;