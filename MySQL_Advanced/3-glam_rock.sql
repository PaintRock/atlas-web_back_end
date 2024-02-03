-- Glam rock as main style by longevity
SELECT band_name, 
    IFNULL(split, 2024) - formed AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', style)
ORDER BY lifespan DESC
;